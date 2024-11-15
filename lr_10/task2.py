from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

tasks = ['Сделать задание', 'Сдать задание']

@app.route('/task_list/')
def task_list():
    return render_template('task_list.html', tasks=tasks)

@app.route('/task_add/', methods=['GET', 'POST'])
def new_task():
    if request.method == 'POST':
        newtask = request.form['new_task']
        tasks.append(newtask)
        return "Задача добавлена!"
    else:
        return render_template('task_add.html')



if __name__ == '__main__':
    app.run()


