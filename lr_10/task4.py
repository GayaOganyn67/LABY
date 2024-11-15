from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

items = [["A", "B", 123, 456, 789]]

@app.route('/market_list/')
def msrket_list():
    return render_template('market_list.html', items=items)

@app.route('/market_add/', methods=['GET', 'POST'])
def market_new():
    if request.method == 'POST':
        new_item = [request.form['new_name'],
                    request.form['new_desc'],
                    request.form['new_weight'],
                    request.form['new_count'],
                    request.form['new_price']]
        items.append(new_item)
        return "Товар добавлен!"
    else:
        return render_template('market_add.html')



if __name__ == '__main__':
    app.run()

