import cv2
import os
import time
import numpy as np
import face_recognition



class AddFace:

    def __init__(self,ID):
        
        

        kaka = cv2.CascadeClassifier('../DATA/face.xml')

        record = cv2.VideoCapture(0)
        count = 0


            

        name = ID
        name = str(name)
        try:

            os.mkdir('../faces/'+name)

        except FileExistsError:

            pass

        goodNAMES = False
        print("Folder Created as ID ---->  ", name, "\nIn Path -----> " , os.getcwd() )
        time.sleep(3)
        
        
        k = 3
        while True:

            black = np.zeros((600,600,3))
            cv2.putText(black,str(k), (200,400), cv2.FONT_HERSHEY_SIMPLEX, 10, (255,0,255), 15)

            
            
            cv2.imshow("SET",black)

            k-=1

            
            cv2.waitKey(1000)

            if k == 0:
                black = np.zeros((600,600,3))
                cv2.putText(black,"SMILE", (60,350), cv2.FONT_HERSHEY_SIMPLEX, 5, (255,0,255), 15)
                cv2.imshow("SET",black)
                cv2.waitKey(1000)
                
                break
            
        cv2.destroyAllWindows()


        while True:
            
            _ , frame = record.read()
            tosave = frame.copy()
            
            
            
            gry_frame = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY )
            
            
            detection = kaka.detectMultiScale ( gry_frame, 1.2, 5 )
            
            
            if len(detection) != 1:
                pass
            
            else:
                
                x,y,w,h = detection[0]
                landmarks = face_recognition.face_landmarks(frame[y:y+h, x:x+w])
                
                try:
                    for f in list(landmarks[0].values()):
                    
                        for (xf,yf) in f:
                            cv2.circle(frame,(x+xf,y+yf),3,(255,255,70),-1)
                except Exception:
                    
                    print('No Face !')
                
                cv2.rectangle(frame,(x,y), ((x+w), (y+h)), (150,0,0),2)
                
            if cv2.waitKey(1) & 0xff == ord('a'):
                
                try:
                    cv2.imwrite('../faces/'+name +"/"+str(count)+".png", tosave[y:y+h, x:x+w])
                    count += 1
                    
                except Exception:
                    
                    print("No Face found -- Have a Face !!")
                
                
                   
                
                
            cv2.putText(frame, "Samples Taken : {}/3 ".format(count),(10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,200), 2)
                
            
            cv2.imshow("KAKA",frame)
            if count > 2:
                break
            
            if cv2.waitKey(30) & 0xFF == 27:
                break
            
            
        cv2.destroyAllWindows()
        record.release()


