import pymysql as MySQLdb
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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
        self.escrol = ttk.Scrollbar(self,orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=self.escrol.set)
        self.escrol.grid(row=3,column=2,sticky='ns')
        self.boton3 = Button(self, text="eliminar")
        self.boton3['command'] = self.OnClick3
        self.boton3.grid(row=4, column=1, padx=10,pady=10)
        base_de_datos = MySQLdb.connect(user="root", password="123456", host="127.0.0.1", database="agenda_telefonica")
        conexion = base_de_datos.cursor()
        sql = "select * from contactos"
        try:
            conexion.execute(sql)
            for row in conexion.fetchall():
                self.tabla.insert("",'end',iid=str(row[0]),text=str(row[0]),values=(str(row[0]),str(row[1]),str(row[2])))
        except:
            base_de_datos.rollback()
            messagebox.showerror(title="error", message="error de conexion")
        base_de_datos.close()
    def OnClick1(self):
        for row in self.tabla.get_children():
            self.tabla.delete(row)
        base_de_datos = MySQLdb.connect(user="root", password="123456", host="127.0.0.1", database="agenda_telefonica")
        conexion = base_de_datos.cursor()
        sql = "select * from contactos"
        try:
            conexion.execute(sql)
            for row in conexion.fetchall():
                self.tabla.insert("",'end',iid=str(row[0]),text=str(row[0]),values=(str(row[0]),str(row[1]),str(row[2])))
        except:
            base_de_datos.rollback()
            messagebox.showerror(title="error", message="error de conexion")
        base_de_datos.close()
    def OnClick2(self):
        base_de_datos = MySQLdb.connect(user="root", password="123456", host="127.0.0.1", database="agenda_telefonica")
        conexion = base_de_datos.cursor()
        sql = "insert into contactos(nombre,numero) values('%s','%s')" % (self.textfield1.get(),self.textfield2.get())
        try:
            conexion.execute(sql)
            base_de_datos.commit()
            self.OnClick1()
            messagebox.showinfo(title="informacion", message="datos insertados")
            self.textfield1.delete(0, END)
            self.textfield2.delete(0, END)
        except:
            base_de_datos.rollback()
            messagebox.showerror(title="error", message="error de conexion")
        base_de_datos.close()
    def OnClick3(self):
        item = self.tabla.item(self.tabla.focus())
        base_de_datos = MySQLdb.connect(user="root", password="123456", host="127.0.0.1", database="agenda_telefonica")
        conexion = base_de_datos.cursor()
        sql = "delete from contactos where id=%s" % (item['text'])
        try:
            conexion.execute(sql)
            base_de_datos.commit()
            self.OnClick1()
            messagebox.showinfo(title="informacion", message="dato eliminado")
        except:
            base_de_datos.rollback()
            messagebox.showerror(title="error", message="error de conexion o no selecciono registro a eliminar")
        base_de_datos.close()
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
