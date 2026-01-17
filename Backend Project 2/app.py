from flask import Flask, render_template, request

app = Flask(__name__)

# creating a temporary storage 
notes = []

@app.route("/", methods=["GET", "POST"])
def home():
    """
    Home route:
    - GET  -> renders the page
    - POST -> accepts a note from the form and appends it to the list
    """

    if request.method == "POST":
        note = request.form.get("note")

        # Created to avoid empty entries
        if note and note.strip():
            notes.append(note.strip())

    return render_template("home.html", notes=notes)


if __name__ == "__main__":
    app.run(debug=True)

