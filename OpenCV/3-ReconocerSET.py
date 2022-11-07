import cv2
import os
import sys

dataPath = os.path.abspath(os.getcwd()) + '/Data'
templatePath = os.path.abspath(os.getcwd()) + '/Template'

if (not (os.path.exists(templatePath + '/modeloLBPHFace.dat')))  or  (not (os.path.exists(templatePath + '/identificador.txt')))  or  (not os.path.exists(os.path.abspath(os.getcwd()) + '/haarcascade_frontalface_default.xml')) :
    print('No se encontro entrenamiento previo') 
    sys.exit()

#Leemos los identificadores y los mostramos
file1 = open(templatePath + '/identificador.txt', 'r')
Lines = file1.readlines()
print('imagePaths=',Lines)

#Contruimos el Reconocedor con el modelo entrenado
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(templatePath + '/modeloLBPHFace.dat')

cap = cv2.VideoCapture(0) #Capturamos Fotos desde Camara

#Capturamos Fotos desde Video
#if not os.path.exists(os.path.abspath(os.getcwd()) + '/Video.mp4'):
#    print('No se logro encontrar Video.mp4') 
#    sys.exit()
#cap = cv2.VideoCapture(os.path.abspath(os.getcwd()) + '/Video.mp4')

faceClassif = cv2.CascadeClassifier(os.path.abspath(os.getcwd()) + '/haarcascade_frontalface_default.xml') #Template para detectar caras

while True:
	ret,frame = cap.read() #Leemos captura
	if ret == False: break
	#normalizamos el fotograma para la deteccion del rostro
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = gray.copy()
	faces = faceClassif.detectMultiScale(gray,1.3,5)
    #Por cada cara detectada en fotograma ejecutamos:
	for (x,y,w,h) in faces:
	    #recortamos el rostro, lo redimensionamos y ponemos en escala de grises
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
		result = face_recognizer.predict(rostro)
		cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
		#Si la diferencia es menor 70 mostramos el identificador:
		if result[1] < 70:
			cv2.putText(frame, '{}'.format( Lines[result[0]].rstrip('\n') ) ,(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		else:
			cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
	#mostramos fotograma con modificaciones	
	cv2.imshow('frame',frame)
	k = cv2.waitKey(1)
	#Hasta que tengamos 300 fotos o se presion la tecla ESC
	if k == 27:
		break

#Finalizamos todo
cap.release()
cv2.destroyAllWindows()
