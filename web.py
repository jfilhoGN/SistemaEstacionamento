import flask, MySQLdb
from flask_mysqldb import MySQL
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'asafaster'
app.config['MYSQL_DB'] = 'teste_flask'

@app.route('/')
def index():
	cur = mysql.connection.cursor()
	cur.execute("SELECT * from flask")
	data = cur.fetchall()
	return render_template('index.html', data = data)

if __name__ == '__main__':
    app.run(
        host="localhost",
        port=int("5000"),
        debug=True
)
