import wx
import pymysql as MySQLdb

#------------------------Formulario de Edicion----------------------------#
class edicion(wx.Frame):
	def __init__(self, id, nombre, numero):
		no_resize = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
		wx.Frame.__init__(self, None, -1, title="editor de fila", size=(220,150), style=no_resize)
		self.Bind(wx.EVT_CLOSE, self.close)
		panel = wx.Panel(self, -1)
		self.label1 = wx.StaticText(panel, -1, label="Nombre:", pos=(10,10))
		self.textfield1 = wx.TextCtrl(panel, -1, size=(100,30), pos=(110,10))
		self.label2 = wx.StaticText(panel, -1, label="Numero:", pos=(10,45))
		self.textfield2 = wx.TextCtrl(panel, -1, size=(100,30), pos=(110,45))
		self.boton = wx.Button(panel, -1, label="modificar", size=(100,25), pos=(110,80))
		self.Bind(wx.EVT_BUTTON, self.OnClick, self.boton)
		self.id = id
		self.nombre = nombre
		self.numero = numero
		self.textfield1.SetValue(nombre)
		self.textfield2.SetValue(numero)
	def close(self, event):
		self.Show(False) 
	def OnClick(self, event):
		id = self.id
		nombre = self.nombre
		numero = self.numero
		nuevo_nombre = self.textfield1.GetValue()
		nuevo_numero = self.textfield2.GetValue()
		base_de_datos = MySQLdb.connect(user="root", password="123456", host="127.0.0.1", database="agenda_telefonica")
		conexion = base_de_datos.cursor()
		sql = "update contactos set nombre='"+nuevo_nombre+"',numero='"+nuevo_numero+"' where (id='"+id+"')and(nombre='"+nombre+"')and(numero='"+numero+"')"
		try:
			conexion.execute(sql)
			base_de_datos.commit()
			wx.MessageBox("datos modificados", "informacion", wx.OK | wx.ICON_INFORMATION)
		except:
			base_de_datos.rollback()
			wx.MessageBox("error de conexion", "error", wx.OK | wx.ICON_WARNING)
		base_de_datos.close()

#------------------------Lengueta Insertar----------------------------#
class insertar(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		self.label1 = wx.StaticText(self, -1, label="Nombre:", pos=(10,10))
		self.nombre = wx.TextCtrl(self, -1, size=(180,30), pos=(110,10))
		self.label2 = wx.StaticText(self, -1, label="Numero:", pos=(10,45))
		self.numero = wx.TextCtrl(self, -1, size=(180,30), pos=(110,45))
		self.boton = wx.Button(self, -1, label="insertar", size=(180,25), pos=(110,80))
		self.Bind(wx.EVT_BUTTON, self.OnClick, self.boton)
	def OnClick(self, event):
		base_de_datos = MySQLdb.connect(user="root", password="123456", host="127.0.0.1", database="agenda_telefonica")
		conexion = base_de_datos.cursor()
		sql = "insert into contactos(nombre,numero) values('%s','%s')" % (self.nombre.GetValue(),self.numero.GetValue())
		try:
			conexion.execute(sql)
			base_de_datos.commit()
			wx.MessageBox("datos insertados", "informacion", wx.OK | wx.ICON_INFORMATION)
			self.nombre.SetValue("")
			self.numero.SetValue("")
		except:
			base_de_datos.rollback()
			wx.MessageBox("error de conexion", "error", wx.OK | wx.ICON_WARNING)
		base_de_datos.close()

#------------------------Lengueta Mostrar----------------------------#
class mostrar(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		self.boton1 = wx.Button(self, -1, label="actualizar", size=(120,25), pos=(10,10))
		self.boton2 = wx.Button(self, -1, label="editar fila", size=(150,25), pos=(140,10))
		self.boton2.Disable()
		self.Bind(wx.EVT_BUTTON, self.OnClick1, self.boton1)
		self.Bind(wx.EVT_BUTTON, self.OnClick2, self.boton2)
		self.tabla = wx.ListCtrl(self, size=(270,160), pos=(10,45), style=wx.LC_REPORT|wx.BORDER_SUNKEN)
		self.tabla.InsertColumn(0, 'id')
		self.tabla.InsertColumn(1, 'nombre')
		self.tabla.InsertColumn(2, 'numero')
		self.tabla.Bind(wx.EVT_LIST_ITEM_SELECTED, self.editar, self.tabla)
		self.tabla.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.noeditar)
	def OnClick1(self, event):
		self.tabla.DeleteAllItems()
		self.boton2.Disable()
		base_de_datos = MySQLdb.connect(user="root", password="123456", host="127.0.0.1", database="agenda_telefonica")
		conexion = base_de_datos.cursor()
		sql = "select * from contactos"
		try:
			conexion.execute(sql)
			i = 0
			for columna in conexion.fetchall():
				self.tabla.InsertItem(i, str(columna[0]))
				self.tabla.SetItem(i, 1, str(columna[1]))
				self.tabla.SetItem(i, 2, str(columna[2]))
				i += 1
		except:
			base_de_datos.rollback()
			wx.MessageBox("error de conexion", "error", wx.OK | wx.ICON_WARNING)
		base_de_datos.close()
	def OnClick2(self, event):
		id = (self.tabla.GetItem(self.tabla.GetFirstSelected(), 0)).GetText()
		nombre = (self.tabla.GetItem(self.tabla.GetFirstSelected(), 1)).GetText()
		numero = (self.tabla.GetItem(self.tabla.GetFirstSelected(), 2)).GetText()
		software = wx.App()
		ventana = edicion(id, nombre, numero)
		ventana.Show()
		software.MainLoop()
	def editar(self, event):
		self.boton2.Enable()
	def noeditar(self, event):
		self.boton2.Disable()
		
#------------------------Formulario para Insertar y Mostrar----------------------------#
class wxpython(wx.Frame):
	def __init__(self):
		no_resize = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
		wx.Frame.__init__(self, None, -1, title="base de datos", size=(310,310), style=no_resize)
		self.Bind(wx.EVT_CLOSE, self.close)
		panel = wx.Panel(self, -1)
		notebook = wx.Notebook(panel)
		panel1 = insertar(notebook)
		panel2 = mostrar(notebook)
		notebook.AddPage(panel1, "insertar")
		notebook.AddPage(panel2, "mostrar")
		sizer = wx.BoxSizer()
		sizer.Add(notebook, 1, wx.EXPAND)
		panel.SetSizer(sizer)
	def close(self, event):
		self.Destroy()


if __name__ == "__main__":
	aplicacion = wx.App()
	formulario = wxpython()
	formulario.Show()
	aplicacion.MainLoop()


