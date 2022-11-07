import cv2
import os
import numpy as np
import sys
import shutil

templatePath = os.path.abspath(os.getcwd()) + '/Template'
dataPath = os.path.abspath(os.getcwd()) + '/Data'
# si la carpet de para entrenar no existe, terminamos proceso
if not os.path.exists(dataPath):
    print('No se logro encontrar set de fotos para Entrenar') 
    sys.exit()

if os.path.exists(templatePath):
    shutil.rmtree(templatePath)
os.makedirs(templatePath)
    
peopleList = os.listdir(dataPath)
print('Lista de personas: ', peopleList) #conjuto de rostros con los que aprender

labels = [] #identificador o etiqueta
facesData = [] #rostros
label = 0 #contador

file_object = open(templatePath + '/identificador.txt', 'a')




# Close the file



#por cada carpeta ejecutamos:
for nameDir in peopleList:
	personPath = dataPath + '/' + nameDir
	file_object.write(nameDir + '\n')
	print('Leyendo las imágenes')
    #por cada foto en la carpet ejecutamos:
	for fileName in os.listdir(personPath):
		print('Rostros: ', nameDir + '/' + fileName)
		labels.append(label)
		facesData.append(cv2.imread(personPath+'/'+fileName,0))
	label = label + 1

file_object.close()
#creamos el reconocedor
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
print("Entrenando...")
#entrenamos con los rosotro y le idicamo un nombre o identificador
face_recognizer.train(facesData, np.array(labels))
#generamos el modelo de reconocimiento
face_recognizer.write(templatePath + '/modeloLBPHFace.dat')
print("Modelo almacenado...")

