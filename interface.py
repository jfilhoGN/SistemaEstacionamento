# !/usr/bin/python
#-*- encoding: utf-8 -*-
import time
from Tkinter import *
from PIL import ImageTk, Image
import MySQLdb, tkMessageBox, serial, threading, tkFont
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="asafaster",
                     db="SistemaEstacionamento")

class Janela():
		def __init__ (self,toplevel):
			self.frame=Frame()		
			self.frame.pack()		
			self.fonte = tkFont.Font(family="", size=10)
			
			self.container=Frame()
			self.container.pack()
			self.container.place(x=470, y=130)
			
			self.container1=Frame()
			self.container1.pack()
			self.container1.place(x=470, y=170)
		
			self.login=Button(self.container, text='Login', background="#B0AEAE",fg="black", command = self.tela_login)
			self.login['width']=10
			self.login.pack()		
			
			self.sair=Button(self.container1, text='Sair',background="#B0AEAE",fg="black", command = raiz.destroy)
			self.sair['width']=10
			self.sair.pack()

		# FALTA TERMINAR
		def tela_login(self):
			self.login = Tk()
			self.t = threading.Thread(target=self.leitura_arduino)
			self.t.start()
			Button(self.login, text='Adicionar', background='#4E4E4E', command= self.tela_adicionar).grid(row=40, column = 10, sticky=W, pady=4)
			#Button(self.login, text='Buscar', background='#4E4E4E').grid(row=40, column = 20, sticky=W, pady=4)
			Button(self.login, text='Horário de Pico', background='#4E4E4E', command= self.tela_horario_pico).grid(row=40, column = 30, sticky=W, pady=4)
			#Button(self.login, text='Recarregar', background='#4E4E4E', command= self.refresh).grid(row=40, column = 40, sticky=W, pady=4)

			Label(self.login, text='Total de Vagas', background='#B0AEAE', fg="black").grid(row=80)
			Label(self.login, text='Vagas Ocupadas', background='#B0AEAE', fg="black").grid(row=90)
			Label(self.login, text='Renda Diária', background='#B0AEAE', fg="black").grid(row=100)

			#Fazer o Select de Vagas Ocupadas, numero de vagas total e renda diária
			cursor = db.cursor()
			cursor.execute("SELECT count(*) FROM Vaga")
			self.numlinhas = int(cursor.rowcount)
			lista_total_vagas = Listbox(self.login,width=10,height=1)
			lista_total_vagas.place(x=120,y=35)
			for x in range(0,self.numlinhas):
				row = cursor.fetchone()
				lista_total_vagas.insert(END,row[0])

			cursor.execute("SELECT count(*) from Vaga where ocupada = 1;")
			numlinhas = int(cursor.rowcount)
			self.lista_vagas_ocupadas = Listbox(self.login,width=10,height=1)
			self.lista_vagas_ocupadas.place(x=120,y=55)
			for x in range(0,numlinhas):
				row = cursor.fetchone()
				self.lista_vagas_ocupadas.insert(END,row[0])
			

			self.renda_diaria = 0
			#numlinhas = int(cursor.rowcount)
			self.lista_renda_diarias = Listbox(self.login,width=10,height=1)
			self.lista_renda_diarias.place(x=120,y=75)
			self.lista_renda_diarias.insert(END,self.renda_diaria)
			self.refresh()
			self.login.geometry('800x460')
			self.login.configure(background='#B0AEAE')

		# FALTA TERMINAR
		def tela_horario_pico(self):
			horario_pico = Tk()
			Label(horario_pico, text='Horário de Pico', background='#B0AEAE', fg="black").grid(row=80)

			#Fazer o Select de Vagas Ocupadas, numero de vagas total e renda diária
			#cursor = db.cursor()
			#cursor.execute("SELECT * FROM ")
			#numlinhas = int(cursor.rowcount)
			lista_horario_pico = Listbox(horario_pico,width=20,height=1)
			lista_horario_pico.place(x=100,y=2)
			# for x in range(0,numlinhas):
			# 	row = cursor.fetchone()
			# 	lista_horario_pico.insert()

			# self.entry_horario_pico = Entry(horario_pico)
			# self.entry_horario_pico.grid(row=100, column=10)

			#Fazer o Select de horario de pico
			
			Button(horario_pico, text='OK', command=horario_pico.destroy, background='#4E4E4E', fg="black").grid(row=100, column = 30, sticky=W, pady=4)
			
			horario_pico.geometry('400x260')
			horario_pico.configure(background='#B0AEAE')


		def tela_adicionar(self):
			adicionar_vagas = Tk()
			Label(adicionar_vagas, text='Valor vaga por hora', background='#B0AEAE', fg="black").grid(row=90)
			Label(adicionar_vagas, text='Local', background='#B0AEAE', fg="black").grid(row=100)

			self.valor_vaga=Entry(adicionar_vagas)
			self.valor_vaga.grid(row=90, column=10)

			self.local=Entry(adicionar_vagas)
			self.local.grid(row=100, column=10)

			Button(adicionar_vagas, text='OK', command=self.update_adicionar, background='#4E4E4E', fg="black").grid(row=100, column = 30, sticky=W, pady=4)
			adicionar_vagas.geometry('400x260')
			adicionar_vagas.configure(background='#B0AEAE')

		# FALTA TERMINAR ----- IMPRIMIR CAIXA DE DIALOGO
		def update_adicionar(self):
			cursor = db.cursor()
			valor_vaga1 = self.valor_vaga.get()
			local1 = self.local.get()
			cursor.execute("SELECT nomeVaga FROM Vaga where nomeVaga = %s",(local1, ))
			numlinhas = cursor.fetchall()
			if len(numlinhas) == 0:
				cursor.execute("INSERT INTO Vaga(nomeVaga, valorPorVaga, ocupada) values (%s,%s,%s)",(local1, valor_vaga1,0))
				db.commit()
				tkMessageBox.showinfo("Mensagem", "Vaga Adicionada com sucesso!")
			else:
				cursor.execute("UPDATE Vaga SET nomeVaga=%s, valorPorVaga=%s WHERE nomeVaga =%s",(local1, valor_vaga1, local1))
				db.commit()
				tkMessageBox.showinfo("Mensagem", "Vaga Atualizada com sucesso!")


		def leitura_arduino(self):
			#Parte de Conexão arduino 
			cursor1 = db.cursor()
			cursor2 = db.cursor()
			ser = serial.Serial('/dev/ttyUSB0', 9600)
			ser.write('5')
			cursor1.execute("SELECT valorPorVaga from Vaga")
			valor_por_vaga = cursor1.fetchall()
			valor_por_segundo = valor_por_vaga[0][0]/3600
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


		def refresh(self):
			self.lista_vagas_ocupadas.delete(0,END)
			cursor = db.cursor()
			cursor.execute("SELECT count(*) from Vaga where ocupada = 1;")
			numlinhas = int(cursor.rowcount)
			self.lista_vagas_ocupadas.place(x=120,y=55)
			for x in range(0,numlinhas):
				row = cursor.fetchone()
				self.lista_vagas_ocupadas.insert(END,row[0])
			# self.lista_renda_diarias.delete(0,END)
			# self.lista_renda_diarias.insert(END,self.renda_diaria)
			self.login.after(1000,self.refresh)

            		  
 
if __name__ == '__main__':
	#Inicialização da aplicação
	raiz=Tk()
	background_image= ImageTk.PhotoImage(Image.open("estacionamento.jpg")) 
	background_label = Label(raiz, image=background_image) 
	background_label.place(x=0, y=0, relwidth=1, relheight=1)
	Janela(raiz) 
	raiz.geometry('810x473')
	#raiz.after_idle(janela.refresh)
	raiz.mainloop()