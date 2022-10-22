from bottle import default_app, route,template
import sqlite3

connection = sqlite3.connect("Phones_list.db")

@route('/')
def hello_world():
    return 'Hello from Kaushik Thumma!'

@route('/hi')
def hi_world():
    return 'Hi from Kaushik Thumma!'

@route('/bye')
def bye_world():
    return 'Bye from Kaushik Thumma!'

@route('/list')
def get_list():
    cursor = connection.cursor()
    rows = cursor.execute("select id, description from list")
    rows = list(rows)
    rows = [{'id':row[0] , 'desc':row[1]} for row in rows]
    return template("Phones_list.tpl", name = "Kaushik Thumma",Phones_list=rows)

application = default_app()

