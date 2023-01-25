import utils
import requests
from flask import Flask, session, render_template, g


app = Flask(__name__)
app.secret_key = 'super secret'

@app.route('/')
def index():
    tasks = utils.date_format_dict(requests.get('http://localhost:8080/api/v1/reminders').json())
    print(tasks)
    history = requests.get('http://localhost:8080/api/v1/histories').json()
    history = history[::-1]
    return render_template('index.html', reminders = tasks, history = history)

if __name__ == '__main__':
    app.run(debug=False)