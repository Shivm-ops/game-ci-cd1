import os
from flask import Flask, render_template, request, session
import random

# Triggering the workflow one last time
app = Flask(__name__)
# A secret key is needed to use sessions in Flask
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def guess_game():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0

    message = ""
    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            session['attempts'] += 1
            if guess < session['number']:
                message = "Too low! Try again."
            elif guess > session['number']:
                message = "Too high! Try again."
            else:
                message = f"Congratulations! You guessed it in {session['attempts']} attempts. A new number has been generated."
                # Reset the game
                session['number'] = random.randint(1, 100)
                session['attempts'] = 0
        except (ValueError, KeyError):
            message = "Please enter a valid number."

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))