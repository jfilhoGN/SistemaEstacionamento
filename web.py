import flask, MySQLdb, time
from flask_mysqldb import MySQL
from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory

app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'asafaster'
app.config['MYSQL_DB'] = 'SistemaEstacionamento'
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods = ['GET'])
def index():
	cur = mysql.connection.cursor()
	cur.execute("SELECT nomeVaga, ocupada from Vaga")
	data = cur.fetchall()
	# valor = []
	# for x in data:
	# 	valor.append(str(x[0]))
	return render_template('index.html', data = data)


if __name__ == '__main__':
	app.run(
    host="localhost",
    port=int("5000"),
    debug=True
	)
   	 
