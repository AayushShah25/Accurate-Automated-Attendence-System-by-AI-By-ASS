
import tkinter as tk
import Add_face
import Add_Face_For_Improve
import ShowDetails
import MainPage
from tkinter import messagebox

class Capture:
    def __init__(self,Details, StartFrom = None):

        def StartCapturing():
            top.destroy()
            
            if StartFrom == None:
                Add_face.AddFace(Details[0])
                ShowDetails.Show(Details)
            else:
                
                print('Getting Face')
                Add_Face_For_Improve.AddFace(Details,StartFrom)
                print('First ENTERD')
                messagebox.showinfo("TRAIN FOR GOOD RESULTS", "The New faces are added, plese go ahead and Re-Train the model to improve accuracy.")
                MainPage.MAINCALL()
                





        top = tk.Toplevel()
        top.geometry("600x500")
       
        
        top.resizable(0, 0)
        top.title("Take Photos")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.183, rely=0.079, height=81, width=394)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Product Sans} -size 28 -weight normal")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Have the candidate''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.317, rely=0.216, height=88, width=233)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Product Sans} -size 48 -weight bold")
        self.Label2.configure(foreground="#800040")
        self.Label2.configure(text='''READY,''')

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.183, rely=0.373, height=41, width=394)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Product Sans} -size 28")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''In front of the Camera''')

        self.Button1 = tk.Button(top,command=StartCapturing)
        self.Button1.place(relx=0.35, rely=0.589, height=84, width=197)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#800040")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Product Sans} -size 30 -weight normal ")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Begin''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.3, rely=0.845, height=30, width=254)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Product Sans} -size 14 -weight normal " )
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Make Different poses please...''')

        top.mainloop()





