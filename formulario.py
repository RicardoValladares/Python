import wx
import sys

class wxpython(wx.Frame):
	def __init__(self):
		no_resize = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
		wx.Frame.__init__(self, None, -1, title="Elementos de un Formulario", size=(385,535), style=no_resize)
		panel = wx.Panel(self, -1)
		#creamos los objetos#
		self.label1 = wx.StaticText(panel, -1, label="Ingrese su nombre:", pos=(10,10))
		self.nombre = wx.TextCtrl(panel, -1, size=(140,25), pos=(230,10))
		self.label2 = wx.StaticText(panel, -1, label="Ingrese su password:", pos=(10,40))
		self.password = wx.TextCtrl(panel, -1, size=(140,25), pos=(230,40), style=wx.TE_PASSWORD)
		self.bandera = wx.Image("sv.png", wx.BITMAP_TYPE_ANY)
		#Python >= Version 3
		if sys.hexversion >= 0x3000000:
			self.imagen = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap(self.bandera), pos=(60,105))
		else: 
			self.imagen = wx.StaticBitmap(panel, wx.ID_ANY, wx.BitmapFromImage(self.bandera), pos=(60,105))
		self.label3 = wx.StaticText(panel, -1, label="Elige tu pais:", pos=(10,70))
		self.pais = wx.ComboBox(panel, -1, pos=(230,70), size=(140,-1), choices=["El Salvador","Guatemala","Honduras","Mexico"], style=wx.CB_READONLY)
		self.Bind(wx.EVT_COMBOBOX, self.OnSelect)
		self.pais.SetSelection(0)
		self.label4 = wx.StaticText(panel, -1, label="Seleccione su rango de edad:", pos=(10,265))
		self.edad1 = wx.RadioButton(panel, label="Mayor de edad", pos=(225,265), style = wx.RB_GROUP)
		self.edad2 = wx.RadioButton(panel, label="Menor de edad", pos=(225,290))
		self.label5 = wx.StaticText(panel, -1, label="Seleccione sus intereses:", pos=(10,325))
		self.interes1 = wx.CheckBox(panel, label="Juegos", pos=(230,325))
		self.interes2 = wx.CheckBox(panel, label="Programas", pos=(230,350))
		self.label6 = wx.StaticText(panel, -1, label="Ingrese una breve descripcion:", pos=(10,390))
		self.descripcion = wx.TextCtrl(panel, -1, style=wx.TE_MULTILINE, size=(145,65), pos=(230,390))
		self.boton1 = wx.Button(panel, -1, label="capturar datos", size=(365,25), pos=(10,465))
		self.Bind(wx.EVT_BUTTON, self.OnClick1, self.boton1)
		self.datos = wx.TextCtrl(panel, -1, style=wx.TE_MULTILINE, size=(365,445), pos=(10,10))#bloqueado
		self.boton2 = wx.Button(panel, -1, label="regresar atras", size=(365,25), pos=(10,465))#bloqueado
		self.Bind(wx.EVT_BUTTON, self.OnClick2, self.boton2)
		#bloqueamos objetos#
		self.datos.Hide()
		self.boton2.Hide()
	#funcion que se activa al presionar un boton1#
	def OnClick1(self, event):
		nombre = self.nombre.GetValue()
		password = self.password.GetValue()
		pais = self.pais.GetValue()
		edad = ""
		if self.edad1.GetValue():
			edad = "Mayor de edad"
		if self.edad2.GetValue():
			edad = "Menor de edad"
		intereses = ""
		if self.interes1.GetValue():
			intereses = "Juegos "
		if self.interes2.GetValue():
			intereses = intereses + "Programas"
		descripcion = self.descripcion.GetValue()
		#metemos los datos en una textarea#
		self.datos.SetValue("Nombre: " + nombre + "\n" + "Password: " + password + "\n" + "Pais: " + pais + "\n" + "Rango de edad: " + edad + "\n" + "Intereses: " + intereses + "\n" + "Descripcion: " + descripcion + "\n")
		#bloquemos los objetos del formulario#
		self.label1.Hide()
		self.nombre.Hide()
		self.label2.Hide()
		self.password.Hide()
		self.label3.Hide()
		self.pais.Hide()
		self.imagen.Hide()
		self.label4.Hide()
		self.edad1.Hide()
		self.edad2.Hide()
		self.label5.Hide()
		self.interes1.Hide()
		self.interes2.Hide()
		self.label6.Hide()
		self.descripcion.Hide()
		self.boton1.Hide()
		#desbloquemos los objetos de salida de datos#
		self.datos.Show()
		self.boton2.Show()
	#funcion que se activa al presionar un boton2#
	def OnClick2(self, event):
		#bloquemos los objetos de salida de datos#
		self.datos.Hide()
		self.boton2.Hide()
		#desbloquemos los objetos del formulario#
		self.label1.Show()
		self.nombre.Show()
		self.label2.Show()
		self.password.Show()
		self.label3.Show()
		self.pais.Show()
		self.imagen.Show()
		self.label4.Show()
		self.edad1.Show()
		self.edad2.Show()
		self.label5.Show()
		self.interes1.Show()
		self.interes2.Show()
		self.label6.Show()
		self.descripcion.Show()
		self.boton1.Show()
	#funcion que se activa al seleccionar opcion del ComboBox#
	def OnSelect(self, event):
		if event.GetSelection()==0:
			self.bandera = wx.Image("sv.png", wx.BITMAP_TYPE_ANY)
		elif event.GetSelection()==1:
			self.bandera = wx.Image("gt.png", wx.BITMAP_TYPE_ANY)
		elif event.GetSelection()==2:
			self.bandera = wx.Image("ho.png", wx.BITMAP_TYPE_ANY)
		else:
			self.bandera = wx.Image("mx.png", wx.BITMAP_TYPE_ANY)
		#Python >= Version 3
		if sys.hexversion >= 0x3000000:
			self.imagen.SetBitmap(wx.Bitmap(self.bandera))
		else:
			self.imagen.SetBitmap(wx.BitmapFromImage(self.bandera))


if __name__ == '__main__':
	aplicacion = wx.App()
	formulario = wxpython()
	formulario.Show()
	aplicacion.MainLoop()


