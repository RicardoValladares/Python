import cv2
import os

dataPath = os.path.abspath(os.getcwd()) + '/Data'

templatePath = os.path.abspath(os.getcwd()) + '/Template'
#imagePaths = os.listdir(dataPath)
#print('imagePaths=',imagePaths)

file1 = open(templatePath + '/identificador.txt', 'r')
Lines = file1.readlines()
print('imagePaths=',Lines)


face_recognizer = cv2.face.LBPHFaceRecognizer_create()

face_recognizer.read(templatePath + '/modeloLBPHFace.dat')

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('Video.mp4')

faceClassif = cv2.CascadeClassifier(os.path.abspath(os.getcwd()) + '/haarcascade_frontalface_default.xml')



while True:
	ret,frame = cap.read()
	if ret == False: break
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = gray.copy()

	faces = faceClassif.detectMultiScale(gray,1.3,5)

	for (x,y,w,h) in faces:
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
		result = face_recognizer.predict(rostro)

		cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
		# LBPHFace
		if result[1] < 70:
			#cv2.putText(frame, '{}'.format(imagePaths[result[0]]) ,(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
			cv2.putText(frame, '{}'.format( Lines[result[0]].rstrip('\n') ) ,(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		else:
			cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
		
	cv2.imshow('frame',frame)
	k = cv2.waitKey(1)
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
