import cv2
import os
import imutils
import shutil
#import sys

dataPath = os.path.abspath(os.getcwd()) + '/Data'
personPath = dataPath + '/Set' #Set de fotos que guardaremos

#si tenemos residuos del Set anterior lo eliminamos
if os.path.exists(personPath):
    shutil.rmtree(personPath)
os.makedirs(personPath)

cap = cv2.VideoCapture(0) #Capturamos Fotos desde Camara

#Capturamos Fotos desde Video
#if not os.path.exists(os.path.abspath(os.getcwd()) + '/Video.mp4'):
#    print('No se logro encontrar Video.mp4') 
#    sys.exit()
#cap = cv2.VideoCapture(os.path.abspath(os.getcwd()) + '/Video.mp4')

faceClassif = cv2.CascadeClassifier(os.path.abspath(os.getcwd()) + '/haarcascade_frontalface_default.xml') #Template para detectar caras
count = 0 # contador que usaremos hasta 300 fotos

while True:    
    ret, frame = cap.read() #Leemos captura
    if ret == False: break
    frame =  imutils.resize(frame, width=640) #Redimensionamos
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Lo cambiamos a escala de grises
    auxFrame = frame.copy() #Copiamos el fotograma
    faces = faceClassif.detectMultiScale(gray,1.3,5) # En base a la escala de grises detectamos caras
    #Por cada cara detectada en fotograma ejecutamos:
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2) #recortamos los rostros
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC) #redimensionamos
        cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro) #guardamos la foto
        count = count + 1       
    #mostramos fotograma con modificaciones
    cv2.imshow('frame',frame)
    k =  cv2.waitKey(1)
    #Hasta que tengamos 300 fotos o se presion la tecla ESC
    if k == 27 or count >= 300:
        break

#Finalizamos todo
cap.release()
cv2.destroyAllWindows()

#Renombramos la carpeta del Set al Identificador dado
nombre = input('Identificador del rostro: ')
os.rename(personPath, dataPath+'/'+nombre)
