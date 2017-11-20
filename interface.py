# !/usr/bin/python
#-*- encoding: utf-8 -*-
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
			login = Tk()
			#Label(login, text='Id da Equipe', background='#B0AEAE', fg="black").grid(row=10)
			#self.t = threading.Thread(target=self.leitura_arduino)
			#self.t.start()
			Button(login, text='Adicionar', background='#4E4E4E', command= self.tela_adicionar).grid(row=40, column = 10, sticky=W, pady=4)
			Button(login, text='Buscar', background='#4E4E4E').grid(row=40, column = 20, sticky=W, pady=4)
			Button(login, text='Horário de Pico', background='#4E4E4E', command= self.tela_horario_pico).grid(row=40, column = 30, sticky=W, pady=4)
			Button(login, text='Sair', background='#4E4E4E', command= self.fechar_programa).grid(row=40, column = 40, sticky=W, pady=4)

			Label(login, text='Total de Vagas', background='#B0AEAE', fg="black").grid(row=80)
			Label(login, text='Vagas Ocupadas', background='#B0AEAE', fg="black").grid(row=90)
			Label(login, text='Renda Diária', background='#B0AEAE', fg="black").grid(row=100)

			#Fazer o Select de Vagas Ocupadas, numero de vagas total e renda diária
			#cursor = db.cursor()
			#cursor.execute("SELECT * FROM ")
			#numlinhas = int(cursor.rowcount)
			lista_total_vagas = Listbox(login,width=10,height=1)
			lista_total_vagas.place(x=120,y=35)
			# for x in range(0,numlinhas):
			# 	row = cursor.fetchone()
			# 	lista_total_vagas.insert()

			#cursor.execute("SELECT * FROM ")
			#numlinhas = int(cursor.rowcount)
			lista_vagas_ocupadas = Listbox(login,width=10,height=1)
			lista_vagas_ocupadas.place(x=120,y=55)
			# for x in range(0,numlinhas):
			# 	row = cursor.fetchone()
			# 	lista_vagas_ocupadas.insert()

			#cursor.execute("SELECT * FROM ")
			#numlinhas = int(cursor.rowcount)
			lista_renda_diarias = Listbox(login,width=10,height=1)
			lista_renda_diarias.place(x=120,y=75)
			# for x in range(0,numlinhas):
			# 	row = cursor.fetchone()
			# 	lista_vagas_ocupadas.insert()

			login.geometry('800x460')
			login.configure(background='#B0AEAE')

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
			Label(adicionar_vagas, text='Número total de vagas', background='#B0AEAE', fg="black").grid(row=80)
			Label(adicionar_vagas, text='Valor vaga por hora', background='#B0AEAE', fg="black").grid(row=90)
			Label(adicionar_vagas, text='Local', background='#B0AEAE', fg="black").grid(row=100)

			self.numero_vagas=Entry(adicionar_vagas)
			self.numero_vagas.grid(row=80, column=10)

			self.valor_vaga=Entry(adicionar_vagas)
			self.valor_vaga.grid(row=90, column=10)

			self.local=Entry(adicionar_vagas)
			self.local.grid(row=100, column=10)

			Button(adicionar_vagas, text='OK', command=self.update_adicionar, background='#4E4E4E', fg="black").grid(row=100, column = 30, sticky=W, pady=4)
			adicionar_vagas.geometry('400x260')
			adicionar_vagas.configure(background='#B0AEAE')

		# FALTA TERMINAR
		def update_adicionar(self):
			cursor = db.cursor()
			numero_vagas1 = self.numero_vagas.get()
			valor_vaga1 = self.valor_vaga.get()
			local1 = self.local.get()
			#cursor.execute("SELECT local FROM Vaga where local =%s",(self.local))
			cursor.execute("INSERT INTO Vaga(local, valorPorHora, ocupada) values (%s,%s,%s)",(local1, valor_vaga1,"false"))
			db.commit()


		def fechar_programa(self):
			self.raiz.destroy
			#self.t.join()

		# FALTA TERMINAR
		def leitura_arduino(self):
			#Parte de Conexão arduino 
			ser = serial.Serial('/dev/ttyUSB0', 9600)
			ser.write('5')
			#ser.write(b'5') #Prefixo b necessario se estiver utilizando Python 3.X
			while True:
				valor = ser.readline()
				print valor 
            		  
 
if __name__ == '__main__':
	#Inicialização da aplicação
	raiz=Tk()
	background_image= ImageTk.PhotoImage(Image.open("estacionamento.jpg")) 
	background_label = Label(raiz, image=background_image) 
	background_label.place(x=0, y=0, relwidth=1, relheight=1)
	Janela(raiz) 
	raiz.geometry('810x473')
	raiz.mainloop()