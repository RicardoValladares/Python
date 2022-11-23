import tkinter as tk
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



#------------------------inicial----------------------------#
my_w = tk.Tk()
my_w.geometry("300x170")

# evento del boton #
def click():
	try:
		clase = sumar()
		clase.setn1( float(n1.get()) )
		clase.setn2( float(n2.get()) )
		resultado.delete(0, tk.END)
		resultado.insert(0, clase.getsumar())
	except ValueError:
		tk.messagebox.showerror(title="ERROR", message="Introduzca numeros")


label1=tk.Label(my_w,text='Ingrese un numero:')
label1.place(x=10,y=10)
n1=tk.Entry(my_w)
n1.place(x=160,y=10)
label2=tk.Label(my_w,text='Ingrese un numero:')
label2.place(x=10,y=45)
n2=tk.Entry(my_w)
n2.place(x=160,y=45)
boton=tk.Button(my_w, text="sumar", command=click)
boton.place(x=160,y=80)
label3=tk.Label(my_w,text='El resultado es:')
label3.place(x=10,y=115)
resultado=tk.Entry(my_w)
resultado.place(x=160,y=115)
# loop de espera mientras no se cierre el formulario #
my_w.mainloop()

