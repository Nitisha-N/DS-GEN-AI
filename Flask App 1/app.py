from flask import Flask, request, render_template
import random
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/showname')
def show_name():
    # Get name from user
    name = request.args.get('name', '').strip()

    if not name:
        return render_template('index.html')

    # Random fun facts to make users feel welcome
    fun_facts = [
        "Your name gives positive vibes ✨",
        "People with your name are usually creative 🎨",
        "Your name sounds confident 💪",
        "Your name feels friendly 😊",
        "Your name stands out 🌟",
        "Your name has a nice rhythm 🎵"
    ]

    random_fact = random.choice(fun_facts)

    # Time-based greeting (India timezone)
    india_tz = pytz.timezone("Asia/Kolkata")
    hour = datetime.now(india_tz).hour

    if hour < 12:
        greeting = "Good Morning ☀️"
    elif hour < 17:
        greeting = "Good Afternoon 🌤️"
    elif hour < 21:
        greeting = "Good Evening 🌙"
    else:
        greeting = "Good Night 🌌"

    return render_template(
        'index.html',
        name=name.upper(),
        fun_fact=random_fact,
        greeting=greeting
    )

if __name__ == '__main__':
    app.run(debug=True)
    
#On EC2 → we used host='0.0.0.0', port=5000
