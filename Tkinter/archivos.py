from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class App(Tk):
	def __init__(self):
		super().__init__()
		self.geometry("400x300")
		self.title("Manipula archivos")
		self.barra_de_menus = Menu(self)
		self.config(menu=self.barra_de_menus)
		self.menu1 = Menu(self.barra_de_menus, tearoff=0)
		self.menu1.add_command(label="Nuevo", command=self.nuevo)
		self.menu1.add_command(label="Abrir", command=self.abrir)
		self.menu1.add_command(label="Guardar como", command=self.guardar)
		self.menu1.add_separator()
		self.menu1.add_command(label="Cerrar", command=self.quit)
		self.menu2 = Menu(self.barra_de_menus, tearoff=0)
		self.menu2.add_command(label="Ayuda", command=self.sobre)
		self.menu2.add_command(label="Sobre mi", command=self.version)
		self.barra_de_menus.add_cascade(label="Archivo", menu=self.menu1)
		self.barra_de_menus.add_cascade(label="Ayuda", menu=self.menu2)
		self.scrollv = Scrollbar(self)
		self.scrollv.pack(side= RIGHT,fill="y")
		self.scrollh = Scrollbar(self, orient= HORIZONTAL)
		self.scrollh.pack(side= BOTTOM, fill= "x")
		self.texto = Text(self, height= 500, width= 350, yscrollcommand= self.scrollv.set, xscrollcommand = self.scrollh.set, wrap= NONE)
		self.texto.pack(fill = BOTH, expand=0)

	def nuevo(self):
		self.texto.delete(1.0, END)

	def abrir(self):
		selectordearchivo = filedialog.askopenfile(filetypes=(("text files", "*.txt"),("All files", "*.*")))
		if selectordearchivo is not None:
			archivo = open(selectordearchivo.name,'r', encoding='utf-8')
			self.texto.delete(1.0, END)
			self.texto.insert(END, archivo.read())
			archivo.close()

	def guardar(self):
		selectordearchivo = filedialog.asksaveasfile(filetypes=(("text files", "*.txt"),("All files", "*.*")), defaultextension=".txt", mode="w")
		if selectordearchivo is not None:
			archivo = open(selectordearchivo.name,'w', encoding='utf-8')
			archivo.write(self.texto.get(1.0, END))
			archivo.close()

	def sobre(self):
		messagebox.showinfo(title="Sobre mi", message="Creado por: R_A_V_R_")

	def version(self):
		messagebox.showinfo(title="Version", message="Version: 1.0")
	

if __name__ == "__main__":
	app = App()
	app.mainloop()

