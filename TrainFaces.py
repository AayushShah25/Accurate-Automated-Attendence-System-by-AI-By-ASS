import cv2
import numpy as np
import os

from FaceEmmbedings import FaceNet
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from DenseModel import DNN
import mysql.connector as connector




class TrainData:

	def __init__(self):

		mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
		cursor = mydb.cursor()

		q = "SELECT COUNT(ID) FROM USERS where isin=1"

		cursor.execute(q)
		result = cursor.fetchall()

		n_classes= result[0][0]


		Vectorizer = FaceNet()
		model = DNN(n_classes)
		model = model.create()


		faces=[]
		labels=[]


		learning_rate=0.01
		epochs=50


		People = os.listdir('../Faces')

		for num,dirName in enumerate(People):
		    for i in os.listdir('../Faces/'+dirName):
		        img=cv2.imread('../Faces'+'/'+dirName+'/'+i,1)
		        
		        img=cv2.resize(img,(160,160))
		        img=img.astype('float')/255.0
		        img=np.expand_dims(img,axis=0)
		        
		        features=Vectorizer.calculate(img)
		        faces.append(features)
		        labels.append(num)


		faces=np.asarray(faces,dtype='float')

		labels=np.asarray(labels)
		labels=labels.reshape(len(labels),1)

		train_data, test_data, train_labels, test_labels = train_test_split(faces,labels,test_size=0.1,random_state=77)


		train_labels = to_categorical (train_labels , num_classes = n_classes)
		test_labels = to_categorical (test_labels , num_classes = n_classes)


		opt = Adam(lr=learning_rate,decay=learning_rate/epochs)

		model.compile(optimizer=opt ,loss='categorical_crossentropy',metrics=['accuracy'])

		model.fit(train_data,train_labels,epochs=epochs,shuffle='true',validation_data=(test_data,test_labels))
		model.save('../face_recognizer.MODEL')


