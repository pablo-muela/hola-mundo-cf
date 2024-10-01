from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('data.json') as file:
        people = json.load(file)
    return render_template('index.html', people=people)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
