from tkinter import *
from tkinter import ttk

lst = [(1,'Ricardo Valladares',73007300),(2,'Veronica Arias',77007700),(3,'Jorge Carcamo',22002200)]

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("MySQL/MariaDB")
        self.resizable(False, False)
        self.label1 = Label(self, text="Nombre: ")
        self.label1.grid(row=0, column=0, padx=10,pady=10)
        self.textfield1 = Entry(self) 
        self.textfield1.grid(row=0, column=1, padx=10,pady=10)
        self.label2 = Label(self, text="Telefono: ")
        self.label2.grid(row=1, column=0)
        self.textfield2 = Entry(self) 
        self.textfield2.grid(row=1, column=1)
        self.boton1 = Button(self, text="Actualizar")
        self.boton1['command'] = self.OnClick1
        self.boton1.grid(row=2, column=0, padx=10,pady=10)
        self.boton2 = Button(self, text="Insertar")
        self.boton2['command'] = self.OnClick2
        self.boton2.grid(row=2, column=1, padx=10,pady=10)
        self.tabla = ttk.Treeview(self, selectmode ='browse')
        self.tabla.grid(row=3,column=0, padx=10,pady=10, columnspan=2)
        self.tabla['show'] = 'headings' 
        self.columnas=['Id','Nombres','Telefonos']
        self.tabla["columns"] = self.columnas
        for i in self.columnas:
            self.tabla.column(i, width = 100)
        for i in self.columnas:
            self.tabla.heading(i, text =i)
        self.escrol = ttk.Scrollbar(self,orient="vertical", command=self.tabla.yview)#V Scrollbar
        self.tabla.configure(yscrollcommand=self.escrol.set)  # connect to Treeview
        self.escrol.grid(row=3,column=2,sticky='ns')
        self.boton3 = Button(self, text="eliminar")
        self.boton3['command'] = self.OnClick3
        self.boton3.grid(row=4, column=1, padx=10,pady=10)
        for i in range(len(lst)):
            self.tabla.insert("",'end',iid=lst[i][0],text=lst[i][0],values=(lst[i][0],lst[i][1],lst[i][2]))
    def OnClick1(self):
        for row in self.tabla.get_children():
            self.tabla.delete(row)
    def OnClick2(self):
        self.tabla.insert("",'end',iid=len(self.tabla.get_children())+1,text=len(self.tabla.get_children())+1,values=(len(self.tabla.get_children())+1,self.textfield1.get(),self.textfield2.get()) )       
    def OnClick3(self):
        item = self.tabla.item(self.tabla.focus())
        print(item['text'])#values
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
