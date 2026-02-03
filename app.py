from flask import Flask, request, render_template_string
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)


# Custom text cleaner

class CleanText:
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        if isinstance(X, list):
            X = pd.Series(X)
        return (
            X.astype(str)
             .str.lower()
             .str.replace(r"[^a-z\s]", "", regex=True)
        )


# Load dataset and train model

df = pd.read_csv("badminton.csv")

df.columns = df.columns.str.lower().str.replace(" ", "_")

# Remove neutral reviews
df = df[df["ratings"] != 3]

# Create sentiment label
df["sentiment"] = df["ratings"].apply(lambda x: 1 if x >= 4 else 0)

X = df["review_text"]
y = df["sentiment"]

pipeline = Pipeline([
    ("clean_text", CleanText()),
    ("tfidf", TfidfVectorizer(max_features=3000)),
    ("model", LogisticRegression(max_iter=1000))
])

pipeline.fit(X, y)


# Flask UI

HTML = """
<!doctype html>
<title>Flipkart Sentiment Analysis</title>

<h2>Flipkart Product Review Sentiment Analysis</h2>

<form method="post">
  <textarea name="review" rows="6" cols="60"
  placeholder="Enter your review here"></textarea><br><br>
  <input type="submit">
</form>

{% if result %}
  <h3>{{ result }}</h3>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        review = request.form["review"]
        prediction = pipeline.predict([review])[0]
        result = (
            "Positive (User is satisfied)"
            if prediction == 1
            else "Negative (User is not satisfied)"
        )
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
