from tkinter import *

mi_Entrys= []

lst = [('Ricardo',73007300),('Veronica',77007700),('Jorge',22002200)]
total_rows = len(lst)
total_columns = len(lst[0])

class App(Tk):
	def __init__(self):
		super().__init__()
		self.title("MySQL/MariaDB")
		self.resizable(False, False)
		self.mi_Label = Label(self, text="Nombre: ")
		self.mi_Label.grid(row=0, column=0)
		self.mi_Entry = Entry(self) 
		self.mi_Entry.grid(row=0, column=1)
		self.mi_Label1 = Label(self, text="Telefono: ")
		self.mi_Label1.grid(row=1, column=0)
		self.mi_Entry1 = Entry(self) 
		self.mi_Entry1.grid(row=1, column=1)
		self.boton1 = Button(self, text="Actualizar")
		self.boton1['command'] = self.clicado
		self.boton1.grid(row=2, column=0)
		self.boton2 = Button(self, text="Insertar")
		self.boton2.grid(row=2, column=1)
		for i in range(total_rows):
			for j in range(total_columns):
				mi_Entry = Entry(self, width=20)
				mi_Entry.grid(row=i+3, column=j)
				mi_Entry.insert(END, lst[i][j])
				mi_Entrys.append(mi_Entry)
	def clicado(self):
	    for btn in mi_Entrys:
	        btn.destroy()		


if __name__ == "__main__":
	app = App()
	app.mainloop()

