import wx
import os
import sys

class wxpython(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, title="Manipula archivos", size=(400,300))
		barra_de_menus = wx.MenuBar()
		#creamos el menu1#
		menu1 = wx.Menu()
		opcion1 = menu1.Append(wx.ID_NEW, "Nuevo")
		opcion2 = menu1.Append(wx.ID_OPEN, "Abrir")
		opcion3 = menu1.Append(wx.ID_SAVE, "Guardar como")
		opcion4 = menu1.Append(wx.ID_EXIT, "Cerrar")
		barra_de_menus.Append(menu1, '&Archivo')
		self.SetMenuBar(barra_de_menus)
		self.Bind(wx.EVT_MENU, self.nuevo, opcion1)
		self.Bind(wx.EVT_MENU, self.abrir, opcion2)
		self.Bind(wx.EVT_MENU, self.guardar, opcion3)
		self.Bind(wx.EVT_MENU, self.salir, opcion4)
		#creamos el menu2#
		menu2 = wx.Menu()
		opcion5 = menu2.Append(wx.ID_HELP, "Version")
		opcion6 = menu2.Append(wx.ID_ABOUT, "Sobre mi")
		barra_de_menus.Append(menu2, '&Ayuda')
		self.SetMenuBar(barra_de_menus)
		self.Bind(wx.EVT_MENU, self.version, opcion5)
		self.Bind(wx.EVT_MENU, self.sobre, opcion6)
		#creamos el area de trabajo#
		self.texto = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.HSCROLL | wx.VSCROLL)
	def nuevo(self, event):
		self.texto.SetValue("")
	def abrir(self, event):
		#Python >= Version 3
		if sys.hexversion >= 0x3000000:
			selectordearchivo = wx.FileDialog(self, "Abrir", os.path.expanduser("~"), "", "*.txt", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		else:
			selectordearchivo = wx.FileDialog(self, "Abrir", os.path.expanduser("~"), "", "*.txt", wx.OPEN)
		if selectordearchivo.ShowModal() == wx.ID_OK: 
			archivo = open(selectordearchivo.GetPath(),'r')
			self.texto.SetValue(archivo.read()) 
			archivo.close()
	def guardar(self, event):
		#Python >= Version 3
		if sys.hexversion >= 0x3000000:
			selectordearchivo = wx.FileDialog(self, "Guardar como", os.path.expanduser("~"), "", "*.txt", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
		else:
			selectordearchivo = wx.FileDialog(self, "Guardar como", os.path.expanduser("~"), "", "*.txt", wx.SAVE)
		if selectordearchivo.ShowModal() == wx.ID_OK:
			#Python >= Version 3
			if sys.hexversion >= 0x3000000:
				archivo = open(selectordearchivo.GetPath(), mode = 'w', encoding='utf-8')
				archivo.write(self.texto.GetValue())
			else:
				archivo = open(selectordearchivo.GetPath()+".txt",'w')
				archivo.write(str(self.texto.GetValue().encode('utf8')))
			archivo.close()
	def salir(self, event):
		self.Destroy()
	def sobre(self, event):
		wx.MessageBox("Creado por: R_A_V_R_", "Sobre mi", wx.OK | wx.ICON_INFORMATION)
	def version(self, event):
		wx.MessageBox("Version: 1.0", "Version", wx.OK | wx.ICON_INFORMATION)
		
if __name__ == '__main__':
	aplicacion = wx.App()
	formulario = wxpython()
	formulario.Show()
	aplicacion.MainLoop()

