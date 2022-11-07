import wx

#------------------------classe sumar----------------------------#
class sumar:
	#inicializamos variables#
	def __init__(self,n1, n2):
		self.n1 = n1
		self.n2 = n2
		self.suma = 0.0
	def setn1(self, n1):
		self.n1 = n1
	def setn2(self, n2):
		self.n2 = n2
	#metodos get para retornar datos#
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
class wxpython(wx.Frame):
	def __init__(self):
		no_resize = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
		wx.Frame.__init__(self, None, -1, title="Manejo de Clases", size=(270,185), style=no_resize)
		panel = wx.Panel(self, -1)
		#creamos los objetos#
		self.label1 = wx.StaticText(panel, -1, label="Ingrese un numero:", pos=(10,10))
		self.n1 = wx.TextCtrl(panel, -1, size=(100,25), pos=(160,10))
		self.label2 = wx.StaticText(panel, -1, label="Ingrese un numero:", pos=(10,45))
		self.n2 = wx.TextCtrl(panel, -1, size=(100,25), pos=(160,45))
		self.boton = wx.Button(panel, -1, label="sumar", size=(100,25), pos=(160,80))
		self.Bind(wx.EVT_BUTTON, self.OnClick, self.boton)
		self.label3 = wx.StaticText(panel, -1, label="El resultado es:", pos=(10,115))
		self.resultado = wx.TextCtrl(panel, -1, size=(100,25), pos=(160,115))
	def OnClick(self, event):
		try:
			n1 = float(self.n1.GetValue())
			n2 = float(self.n2.GetValue())
			#invocamos la clase sumar#
			clase = sumar(n1,n2)
			#usamos una funcion get de la clase sumar#
			self.resultado.SetValue(str(clase.getsumar()))
		except ValueError:
			wx.MessageBox("Introduzca numeros", "ERROR", wx.OK | wx.ICON_WARNING)


if __name__ == '__main__':
	aplicacion = wx.App()
	formulario = wxpython()
	formulario.Show()
	aplicacion.MainLoop()
	
