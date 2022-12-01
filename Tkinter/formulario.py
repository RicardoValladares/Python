from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

class App(Tk):
	def __init__(self):
		super().__init__()
		self.geometry("385x535")
		self.title("Elementos de un Formulario")
		self.resizable(False, False)
		self.label1=Label(self,text='Ingrese su nombre:')
		self.label1.place(x=10,y=10)
		self.nombre=Entry(self, width=19)
		self.nombre.place(x=230,y=10)
		self.label2=Label(self,text='Ingrese su password:')
		self.label2.place(x=10,y=40)
		self.password=Entry(self, width=19, show="*")
		self.password.place(x=230,y=40)
		self.label3=Label(self,text='Elige tu pais:')
		self.label3.place(x=10,y=70)
		self.pais = ttk.Combobox(self,state="readonly", width=19, values=["El Salvador","Guatemala","Honduras","Mexico"])
		self.pais.bind("<<ComboboxSelected>>", self.OnSelect)
		self.pais.place(x=230,y=70)
		self.pais.set("El Salvador")
		self.bandera = PhotoImage(file='./sv.png')
		self.imagen = Label(self, image=self.bandera)
		self.imagen.place(x=60,y=105)
		self.label4=Label(self,text="Seleccione su rango de edad:")
		self.label4.place(x=10,y=265)
		self.opcionradio = IntVar()
		self.edad1 = Radiobutton(self, text="Mayor de edad", variable=self.opcionradio, value=0)
		self.edad2 = Radiobutton(self, text="Menor de edad", variable=self.opcionradio, value=1)
		self.edad1.place(x=225,y=265)
		self.edad2.place(x=225,y=290)
		self.label5 = Label(self,text="Seleccione sus intereses:") 
		self.label5.place(x=10,y=325)
		self.opcioncheck1 = IntVar()
		self.interes1 = Checkbutton(self, text="Juegos", variable=self.opcioncheck1)
		self.interes1.place(x=230, y=325)
		self.opcioncheck2 = IntVar()
		self.interes2 = Checkbutton(self, text="Programas", variable=self.opcioncheck2)
		self.interes2.place(x=230, y=350)
		self.label6 = Label(self,text="Ingrese una breve descripcion:") 
		self.label6.place(x=10,y=390)
		self.descripcion = scrolledtext.ScrolledText(self, wrap=WORD, width=15, height=3)
		self.descripcion.place(x=230,y=390)
		self.boton1=Button(self, text="capturar datos", width=50)
		self.boton1['command'] = self.OnClick1
		self.boton1.place(x=10,y=465)
		self.datos = scrolledtext.ScrolledText(self, wrap=WORD, width=40, height=25)#bloqueado
		self.datos.place(x=10,y=10)
		self.datos.place_forget()
		self.boton2 = Button(self, text="regresar atras", width=50)#bloqueado
		self.boton2['command'] = self.OnClick2
		self.boton2.place(x=10,y=465)
		self.boton2.place_forget()

	def OnClick1(self):
		edad = ""
		intereses = ""
		if self.opcionradio.get()==0:
			edad = "Mayor de edad"
		else:
			edad = "Menor de edad"
		if self.opcioncheck1.get():
			intereses = "Juegos"
		if self.opcioncheck2.get():
			intereses = intereses+" Programas"
		self.datos.delete(1.0, END)
		self.datos.insert(END, "Nombre: "+self.nombre.get()+"\n"+"Password: " +self.password.get()+"\n"+"Pais: " +self.pais.get()+ "\n" + "Rango de edad: " +edad+ "\n" + "Intereses: " +intereses+ "\n" + "Descripcion: "+ self.descripcion.get(1.0, END) +"\n")
		self.label1.place_forget()
		self.nombre.place_forget()
		self.label2.place_forget()
		self.password.place_forget()
		self.label3.place_forget()
		self.pais.place_forget()
		self.imagen.place_forget()
		self.label4.place_forget()
		self.edad1.place_forget()
		self.edad2.place_forget()
		self.label5.place_forget()
		self.interes1.place_forget()
		self.interes2.place_forget()
		self.label6.place_forget()
		self.descripcion.place_forget()
		self.boton1.place_forget()
		self.datos.place(x=10,y=10)
		self.boton2.place(x=10,y=465)

	def OnClick2(self):
		self.datos.place_forget()
		self.boton2.place_forget()
		self.label1.place(x=10,y=10)
		self.nombre.place(x=230,y=10)
		self.label2.place(x=10,y=40)
		self.password.place(x=230,y=40)
		self.label3.place(x=10,y=70)
		self.pais.place(x=230,y=70)
		self.imagen.place(x=60,y=105)
		self.label4.place(x=10,y=265)
		self.edad1.place(x=225,y=265)
		self.edad2.place(x=225,y=290)
		self.label5.place(x=10,y=325)
		self.interes1.place(x=230, y=325)
		self.interes2.place(x=230, y=350)
		self.label6.place(x=10,y=390)
		self.descripcion.place(x=230,y=390)
		self.boton1.place(x=10,y=465)
	
	def OnSelect(self, event):
		if self.pais.get()=="El Salvador":
			self.bandera = PhotoImage(file='sv.png')
		elif self.pais.get()=="Guatemala":
			self.bandera = PhotoImage(file='gt.png')
		elif self.pais.get()=="Honduras":
			self.bandera = PhotoImage(file='ho.png')
		else:
			self.bandera = PhotoImage(file='mx.png')
		self.imagen.configure(image=self.bandera)
		self.imagen.image = self.bandera


if __name__ == "__main__":
	app = App()
	app.mainloop()
