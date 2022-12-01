from tkinter import *
from tkinter import messagebox


#------------------------classe sumar----------------------------#
class sumar:
	#inicializamos variables#
	def __init__(self):
		self.n1 = 0.0
		self.n2 = 0.0
		self.suma = 0.0
	#metodos set#
	def setn1(self, n1):
		self.n1 = n1
	def setn2(self, n2):
		self.n2 = n2
	#metodos get#
	def getsumar(self): 
		self.suma=self.n1+self.n2
		return str(self.n1) + "+" + str(self.n2) + "=" + str(self.suma)
	def getn1(self): 
		return str(self.n1)
	def getn2(self): 
		return str(self.n2)
	def getsuma(self):
		self.suma=self.n1+self.n2 
		return str(self.suma)


#------------------------classe App----------------------------#
class App(Tk):
	def __init__(self):
		super().__init__()
		self.geometry("300x170")
		self.title("Manejo de Clases")
		self.resizable(False, False)
		self.label1=Label(self,text='Ingrese un numero:')
		self.label1.place(x=10,y=10)
		self.n1=Entry(self, width=18)
		self.n1.place(x=160,y=10)
		self.label2=Label(self,text='Ingrese un numero:')
		self.label2.place(x=10,y=45)
		self.n2=Entry(self, width=18)
		self.n2.place(x=160,y=45)
		self.boton=Button(self, text="sumar", width=15)
		self.boton['command'] = self.click
		self.boton.place(x=160,y=80)
		self.label3=Label(self,text='El resultado es:')
		self.label3.place(x=10,y=115)
		self.resultado=Entry(self, width=18)
		self.resultado.place(x=160,y=115)
	
	def click(self):
		try:
			#invocamos la clase sumar#
			clase = sumar()
			#usamos funciones set de la clase sumar#
			clase.setn1( float(self.n1.get()) )
			clase.setn2( float(self.n2.get()) )
			self.resultado.delete(0, END)
			#usamos funciones get de la clase sumar#
			self.resultado.insert(0, clase.getsumar())
		except ValueError:
			messagebox.showerror(title="ERROR", message="Introduzca numeros")


#------------------------ejecutamos si estamos en la ejecucion principal----------------------------#
if __name__ == "__main__":
	app = App()
	app.mainloop()

