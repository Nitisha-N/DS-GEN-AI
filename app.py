from flask import Flask, render_template, request, redirect
from models import db, URLMap
from services import is_valid_url, generate_short_code

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# HOME PAGE
@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None
    error = None

    if request.method == 'POST':
        original_url = request.form['original_url']

        if not is_valid_url(original_url):
            error = "Please enter a valid URL"
        else:
            short_code = generate_short_code()

            while URLMap.query.filter_by(short_code=short_code).first():
                short_code = generate_short_code()

            new_url = URLMap(
                original_url=original_url,
                short_code=short_code
            )

            db.session.add(new_url)
            db.session.commit()

            short_url = request.host_url + short_code

    return render_template('index.html', short_url=short_url, error=error)


# REDIRECT ROUTE
@app.route('/<short_code>')
def redirect_url(short_code):
    url_entry = URLMap.query.filter_by(short_code=short_code).first_or_404()
    return redirect(url_entry.original_url)


# HISTORY PAGE
@app.route('/history')
def history():
    urls = URLMap.query.order_by(URLMap.created_at.desc()).all()
    return render_template('history.html', urls=urls)


if __name__ == '__main__':
    app.run(debug=True)
