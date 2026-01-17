** Regex Matcher Application (Flask) **

This project is a simple Flask-based web application that replicates the core functionality of regex testing tool - regex101.

## Objective
The objective of this project is to:
- Accept a test string and a regular expression from the user
- Display all matched substrings on submission
- Handle invalid regular expressions gracefully

## Tech Stack
- Python (Flask)
- HTML
- CSS (internal styling)
- JavaScript

## Project Architecture
- Flask is used as the backend framework to serve the application
- The frontend handles user interaction and regex processing using JavaScript
- This design keeps the backend lightweight while focusing on core logic

## Features
- User input for test string and regex
- Display of all matched strings
- Error handling for invalid regex
- Clean and minimal interface

## How to Run
1. Install Flask:
   ```bash
   pip install flask

2. Run the Flask app:
	python regex.py

3. Open browser and go to:

	http://127.0.0.1:5000/

## Limitations

- Advanced regex features such as explanation and highlighting are not included

- Regex evaluation is handled on the client side for simplicity

** Conclusion **

This project demonstrates the integration of Flask with frontend logic to build a practical regex matching tool while maintaining a focused scope.
