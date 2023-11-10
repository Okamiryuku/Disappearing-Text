from flask import Flask, render_template
from random import choice


app = Flask(__name__)

with open('static/phrases.txt', 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]


@app.route('/')
def index():
    phrases = choice(lines)
    return render_template('index.html', phrases=phrases)


if __name__ == '__main__':
    app.run(debug=True)
