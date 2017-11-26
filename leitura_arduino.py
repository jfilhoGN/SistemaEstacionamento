# !/usr/bin/python
#-*- encoding: utf-8 -*-
import serial, MySQLdb
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="asafaster",
                     db="SistemaEstacionamento")
#Parte de Conexão arduino 
cursor1 = db.cursor()
cursor2 = db.cursor()
ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.write('5')
#ser.write(b'5') #Prefixo b necessario se estiver utilizando Python 3.X
while True:
	valor1 = ser.readline()
	valor2 = ser.readline()
	sensor1 = valor1.split(":")
	sensor2 = valor2.split(":")
	print ("Local " +sensor1[0])
	print ("ocupada " +sensor1[1])
	print ("Local " +sensor2[0])
	print ("ocupada " +sensor2[1])
	cursor1.execute("UPDATE Vaga SET ocupada=%s WHERE nomeVaga =%s",(int(sensor1[1]), sensor1[0]))
	db.commit()
	cursor2.execute("UPDATE Vaga SET ocupada=%s WHERE nomeVaga =%s",(int(sensor2[1]), sensor2[0]))
	db.commit()