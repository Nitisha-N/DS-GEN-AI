import os
import random
import string
from datetime import datetime, timedelta
from urllib.parse import urlparse

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import (
    LoginManager, UserMixin,
    login_user, logout_user,
    login_required, current_user
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config["SECRET_KEY"] = "secretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = "login"


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(9), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    urls = db.relationship("ShortURL", backref="user", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class ShortURL(db.Model):
    __tablename__ = "short_url"

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.Text, nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    domain = db.Column(db.String(255))
    clicks = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def is_valid_url(url):
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and parsed.netloc


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if len(username) < 5 or len(username) > 9:
            flash("Username must be between 5 to 9 characters", "error")
            return redirect(url_for("register"))

        if User.query.filter_by(username=username).first():
            flash("This username already exists", "error")
            return redirect(url_for("register"))

        user = User(username=username)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash("Registration successful. Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            flash("Invalid username or password", "error")
            return redirect(url_for("login"))

        login_user(user)
        flash("Login successful", "success")
        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "success")
    return redirect(url_for("login"))


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    if request.method == "POST":
        original_url = request.form.get("original_url", "").strip()
        expiry_days = request.form.get("expiry", "").strip()

        if not is_valid_url(original_url):
            flash("Please enter a valid URL (http or https)", "error")
            return redirect(url_for("dashboard"))

        expires_at = None
        if expiry_days.isdigit():
            expires_at = datetime.utcnow() + timedelta(days=int(expiry_days))

        short_code = generate_short_code()

        short_url = ShortURL(
            original_url=original_url,
            short_code=short_code,
            domain=urlparse(original_url).netloc,
            expires_at=expires_at,
            user=current_user
        )

        db.session.add(short_url)
        db.session.commit()

        flash("URL shortened successfully", "success")
        return redirect(url_for("dashboard"))

    urls = (
        ShortURL.query
        .filter_by(user_id=current_user.id)
        .order_by(ShortURL.created_at.desc())
        .all()
    )

    return render_template("dashboard.html", urls=urls)


@app.route("/<short_code>")
def redirect_short_url(short_code):
    url = ShortURL.query.filter_by(short_code=short_code, is_active=True).first()

    if not url:
        return render_template("error.html", message="Invalid or expired link")

    if url.expires_at and datetime.utcnow() > url.expires_at:
        url.is_active = False
        db.session.commit()
        return render_template("error.html", message="This link has expired")

    url.clicks += 1
    db.session.commit()
    return redirect(url.original_url)


if __name__ == "__main__":
    app.run(debug=True)
