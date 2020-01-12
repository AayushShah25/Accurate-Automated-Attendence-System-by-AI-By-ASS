import tkinter as tk
from tkinter import messagebox
import os
import sys
import Names
import mysql.connector as connector
import webbrowser
import Hold
import Remove
import ReList
import numpy as np
from FaceEmmbedings import FaceNet
from keras.models import load_model
import cv2
import FindImprove

class MAINCALL():
    
    model=load_model('../DATA/facenet_keras.h5')

    def __init__(self):

        mydb= connector.connect(host = "localhost", user= "root", passwd = "aayush123", database="testdb")
        cursor = mydb.cursor()

        q = "SELECT COUNT(ID) FROM USERSE"
        cursor.execute(q)
        result = cursor.fetchall()
        incrementedID = int(result[0][0]) + 1


        window = tk.Toplevel()


        window.geometry("700x700")
        window.maxsize(1920, 1080)
        window.resizable(0, 0)
        window.title("Main Page")
        window.configure(background="#d9d9d9")

        #DEFs
        def ExtractFeatures(img):
            
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        
            img = cv2.resize(img, (160,160))
            img = img.reshape((1,160,160,3))
            img = img / 255.0
            
            return self.model.predict(img)[0]
        
        def Improve():
            window.destroy()
            FindImprove.FindForImprove()
            
        def ADD():
            window.destroy()
            Names.EnterData(incrementedID)

        def Removefn():
            window.destroy()
            Remove.RemoveField()

        def showUnkowns():

            try:

                if (webbrowser.open(r'C:\Users\GIGABYTE\Desktop\Project\Unknowns\\')):
                    pass
                else:
                    print (' No File Found Error ')
                    
            except Exception:

                print('Error in opening the Folder ')

        def hold():
            window.destroy()
            Hold.Hold()

        def release():
            window.destroy()
            ReList.ListKAKA()
            
        def Train():

            
            
            
            directories = [ name for name in os.listdir('../Faces') if os.path.isdir(os.path.join('../Faces/', name)) ]
            
            

            if len(directories) > 0:
                
                fix = False
                if messagebox.askyesno("Really ?","There are "+str(len(directories))+" persons, which will take some time to be executed \n Do you want to continue ?"):
                    
                    
                    for personID in directories:
                        print("Checking for Person:" + str(personID))
                        
                        
                        if len(os.listdir('../Faces/'+personID)) > 6 or len(os.listdir('../Faces/'+personID)) < 3:
                            fix = True
                            if len(os.listdir('../Faces/'+personID)) == 0:
                                
                                messagebox.showerror("Make Some Changes !!","No Image Data Found ! Please Click on 'Improve for Training' to proceed ahead for ID :" + str(personID) )
                                break
                            
                            messagebox.showerror("Make Some Changes !!","The number of Faces for ID: "+str(personID)+" Must be in between 3 and 6 (Inclusive)")
                            break
                        
                        
                    if fix == False:        
                        print("Feeding In..." )
                        for personID in directories:        
                            
                            features = []
                            cursor = mydb.cursor()
                            
                            for face in os.listdir('../Faces/'+str(personID)):
                                img = cv2.imread('../Faces/'+str(personID)+"/"+str(face))
                                
                                features.append(ExtractFeatures(img))
                                
                            features = np.array(features)
                            string_code = features.__repr__()
                            
                            
                            
                            q = "update userse set encodings = %s where id = "+str(personID)
                            
                            
                            val = [(string_code,)]
                            cursor.executemany(q,val)
                            mydb.commit()
                            
                        messagebox.showinfo("Done !","The Faces are improved and loaded successfully !")
                                
                                
                                
                            
                                
                        
                        
                        
                        
                        
                    
                    
                    
                    
                
                
            else:
                messagebox.showwarning("No One is there !","There is not a single person to be fed in...\n Please Click Add Person to add one ")
                



        # BUTTONS

        #--------------------------------------------------------------------------------------------

        Btn1 = tk.Button(window,text='Add A Person',
                                        font="-family {Product Sans} -size 14 -weight bold",
                                        command= ADD)
        Btn1.place(relx=0.057, rely=0.043, height=200, width=200)

        #--------------------------------------------------------------------------------------------

        Btn2 = tk.Button(window,text='Remove A Person',
                                        font="-family {Product Sans} -size 14 -weight bold", command=Removefn)
        Btn2.place(relx=0.614, rely=0.043, height=200, width=200)


        #--------------------------------------------------------------------------------------------



        Btn3 = tk.Button(window,text='Show Unknowns',
                                        font="-family {Product Sans} -size 14 -weight bold",
                                        command = showUnkowns)
        Btn3.place(relx=0.057, rely=0.386, height=200, width=200)

          #--------------------------------------------------------------------------------------------

        train = tk.Button(window, text = "Train System", font="-family {Product Sans} -size 14 -weight bold", command=Train, bg = "#800040", fg="#FFFFFF")
        train.place(relx=0.375, rely=0.350, height=100, width=150)


        Improve = tk.Button(window, text = "Improve for Training", font="-family {Product Sans} -size 14 -weight bold", bg = "#800040", fg="#FFFFFF", wraplength="100", command = Improve)
        Improve.place(relx=0.375, rely=0.600, height=100, width=150)
        




        #-------------------

        Btn4 = tk.Button(window,text='Generate Report',
                                        font="-family {Product Sans} -size 14 -weight bold")
        Btn4.place(relx=0.614, rely=0.386, height=200, width=200)
         
         #--------------------------------------------------------------------------------------------

        Btn5 = tk.Button(window,text='Hold a Person for Leave',
                                font="-family {Product Sans} -size 14 -weight bold",wraplength="200",
                                command = hold)

        Btn5.place(relx=0.057, rely=0.701, height=200, width=200)

        #-----------------------------

        Btn6 = tk.Button(window,text='Release a Person from Leave',
                                font="-family {Product Sans} -size 14 -weight bold",wraplength="200",
                                command=release)

        Btn6.place(relx=0.614, rely=0.701, height=200, width=200)





        window.mainloop()
