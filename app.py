from flask import Flask, redirect, render_template, url_for, \
    request
import sql_db
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def start():
    return redirect('index_bootstrap')

@app.route('/index')
def index():
    list = sql_db.showAll()
    return render_template("index.html", list=list)

@app.route('/index_bootstrap')
def index_bootstrap():
    list = sql_db.showAll()
    return render_template("index_bootstrap.html", list=list)

@app.route('/delete_task/<int:id>')
def delete_task(id):
    sql_db.remove(id)
    return redirect(url_for('index_bootstrap'))

@app.route('/insert_task', methods=['POST'])
def insert_task():
    name = request.form['todo']
    if request.form.get('urgent'):
        sql_db.insert_urgent(name)
    else:
        sql_db.insert(name)

    return redirect(url_for('index_bootstrap'))



if __name__ == '__main__':
    app.run()
