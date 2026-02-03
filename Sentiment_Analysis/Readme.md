# Flipkart Sentiment Analysis (Flask + AWS)

This project performs sentiment analysis on Flipkart product reviews and deploys
a Flask web application on AWS EC2 for real-time sentiment prediction.

## Objective
To classify customer reviews as positive or negative based on their ratings and
review text, and provide real-time sentiment analysis through a web interface.

## Dataset
The project uses the provided `badminton.csv` dataset, which contains real
Flipkart reviews for the YONEX MAVIS 350 Nylon Shuttle product.

## Approach
- Text preprocessing using a custom transformer
- TF-IDF for numerical feature extraction
- Logistic Regression for sentiment classification
- Binary sentiment classification:
  - Positive (ratings 4 and 5)
  - Negative (ratings 1 and 2)

Neutral reviews (rating 3) are excluded.

## Web Application
A Flask web application allows users to enter a product review and receive
instant sentiment feedback.

## Deployment
The application is deployed on an AWS EC2 instance and is accessible through a
public IP and port.

## How to Run Locally
```bash
pip install -r requirements.txt
python app.py

Then open:

http://localhost:5000

Tech Stack

Python

Flask

scikit-learn

AWS EC2
