import cv2
import numpy as np
import os
from datetime import date
from datetime import datetime


from keras.models import load_model
from FaceEmmbedings2 import FaceNet
import mysql.connector as connector

#### DATE CHAEKING 

mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
cursor = mydb.cursor()

q  = "select datekaka from checkdate limit 1"

cursor.execute(q)
datecheck = cursor.fetchone()

datecheck = datecheck[0]

var = datetime.now()
todaydate = var.strftime("%d%m%y")
print(datecheck)
print(todaydate)


if datecheck == todaydate:
    pass

else:

    #### TRUNCATE 
    mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
    cursor = mydb.cursor()

    q = "TRUNCATE attendance";

    cursor.execute(q)
    mydb.commit()

    #### ENTER DATA

    mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
    cursor = mydb.cursor()

    q = "insert into attendance(id,name,hold) select id,name,hold from users where isin = 1"

    cursor.execute(q)
    mydb.commit()

    #### Update Date

    mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
    cursor = mydb.cursor()

    q = "update checkdate set datekaka = '"+todaydate+"'"
    print(q)
    cursor.execute(q)
    mydb.commit()

    







#### GET DETAILS

mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
cursor = mydb.cursor()

q = "SELECT name FROM attendance"
cursor.execute(q)
result = cursor.fetchall()

today = date.today()
today = today.strftime("%d-%m-%y")

try:
    os.mkdir('./Unknowns/'+today)
except FileExistsError:
    pass

people = {}



for i,name in enumerate(result):
    
    people[i] = name[0]

print(people)

model=load_model('face_recognizer.MODEL')
cascade = cv2.CascadeClassifier('./data/Face.xml')

label=None
Vectorizer= FaceNet()

record = cv2.VideoCapture(0)


while True:
    
    faces = []
    coordinates = []
    
    _, frame = record.read()
    frame = cv2.flip(frame,1)
    
    gry_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    detect = cascade.detectMultiScale(gry_frame, 1.2, 10)
    
    for x,y,w,h in detect:
        
        faces.append( frame[y:y+h, x:x+w] )
        coordinates.append((x,y,w,h))
        
    
    
    
    

    if(faces is not None):
        for i in range(len(faces)):
            face1 = faces[i]
            
            coordinate =coordinates[i]
            
            FaceIsolated = face1

            face1 =cv2.resize(face1,(160,160))
           
            face1=face1.astype('float')/255.0
            face1=np.expand_dims(face1,axis=0)

            feed=Vectorizer.calculate(face1)
            feed=np.expand_dims(feed,axis=0)
            
            prediction=model.predict(feed)[0]

            result=int(np.argmax(prediction))
            
            if(np.max(prediction)>0.9999):
                for i in people:
                    
                    if(result==i):
                        
                        label=people[i]

                        pos = int(result)+1
                        check = "select attend from attendance where ID ="+str(pos)
                        cursor = mydb.cursor()
                        cursor.execute(check)
                        result = cursor.fetchall()
                        
                        if result[0][0] == 1:
                            label=people[i]+" You are Present !!! Go Home !"
                        elif ( result[0][0] == None or result[0][0] == 0 ):

                            checkforHold = "select hold from attendance where id="+str(pos)
                            cursor = mydb.cursor()
                            cursor.execute(checkforHold)
                            resYes = cursor.fetchall()

                            if resYes[0][0] == 0:

                                q = "update attendance set ATTEND = true where id ="+str(pos)

                                cursor = mydb.cursor()
                                cursor.execute(q)
                                mydb.commit()

                            else:

                                label = "Unknown"
                                now= datetime.now()
                                now= now.strftime("%H%M%S")
                                try:

                                    cv2.imwrite("./Unknowns/"+today+"/"+str(now)+".png", FaceIsolated)

                                except Exception:
                                    print('Error in Saving the Unknown face... Please Restart the System.')





                        

                       
                        
            else:
                now= datetime.now()
                now= now.strftime("%H%M%S")
                try:

                    cv2.imwrite("./Unknowns/"+today+"/"+str(now)+".png", FaceIsolated)

                except Exception:
                    print('Error in Saving the Unknown face... Please Restart the System.')
                    
                label='Unknown'
           


            cv2.putText(frame,label,(coordinate[0],coordinate[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,200),2)
            
            cv2.rectangle(frame,(coordinate[0],coordinate[1]),(coordinate[0] + coordinate[2] , coordinate[1] + coordinate[3]),(123,234,1),3)
            
            #cv2.imshow('onlyFace',f)
    cv2.imshow('Recognizition',frame)
    if cv2.waitKey(1) & 0xff == 27 :
        break
record.release()
cv2.destroyAllWindows()



