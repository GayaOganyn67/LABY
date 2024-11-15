from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/index/')
def hello():
    greet = ""
    if 6 <= datetime.now().hour < 12:
        greet = 'Доброе утро'
    elif 12 <= datetime.now().hour < 18:
        greet = 'Добрый день'
    elif 18 <= datetime.now().hour < 24:
        greet = 'Добрый вечер'
    elif 0 <= datetime.now().hour < 6:
        greet = 'Доброй ночи'
    return render_template('index.html', greeting=greet)

if __name__ == '__main__':
    app.run()
