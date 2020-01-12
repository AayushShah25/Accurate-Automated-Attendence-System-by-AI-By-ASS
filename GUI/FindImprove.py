import tkinter as tk
from tkinter import ttk
from tkinter import *
import mysql.connector as connector
import FList





class FindForImprove:
    def __init__(self, top=None):
        
       
        def Find():

            name = self.Entry1.get().title()
            Department= i.get()
            mydb = connector.connect(host="localhost", user ="root", passwd="aayush123" , database="testdb")

			
            cursor = mydb.cursor()

            q = "select * from userse where Name like'%"+str(name)+"%'  and post='"+str(Department)+"' and isin=1 and hold=0"
            print(q)
            cursor.execute(q)
            result = cursor.fetchall()

            print(result)

            if (len(result) == 0 or result == None):
            	messagebox.showinfo("No Result ! ","No match found for the Given info \n Try changing words and post and have an accurate match !")
            else:
            	top.destroy()
            	FList.ListKAKA(result)


        top = tk.Toplevel()

        top.geometry("669x443")
        
        top.resizable(0, 0)
        top.title("Improve Face Finder")
        top.configure(background="#d9d9d9")

        
        

        self.NAMELabel = tk.Label(top,background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Product Sans} -size 15 -weight bold ",foreground="#000000",text='''Name''')
        self.NAMELabel.place(relx=0.105, rely=0.293, height=51, width=104)
        

        self.DEPARTlabel = tk.Label(top)
        self.DEPARTlabel.place(relx=0.049, rely=0.474, height=41, width=134)
        self.DEPARTlabel.configure(activebackground="#f9f9f9")
        self.DEPARTlabel.configure(activeforeground="black")
        self.DEPARTlabel.configure(background="#d9d9d9")
        self.DEPARTlabel.configure(disabledforeground="#a3a3a3")
        self.DEPARTlabel.configure(font="-family {Product Sans} -size 15 -weight bold")
        self.DEPARTlabel.configure(foreground="#000000")
        self.DEPARTlabel.configure(highlightbackground="#d9d9d9")
        self.DEPARTlabel.configure(highlightcolor="black")
        self.DEPARTlabel.configure(text='''Department''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.314, rely=0.293,height=50, relwidth=0.574)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")



        i = StringVar(top)
        posts = ["Accountant", "Cashier", "Worker", "Manager"]
        self.TCombobox1 = ttk.Combobox(top,value=posts)
        self.TCombobox1.place(relx=0.314, rely=0.474, relheight=0.093
                , relwidth=0.274)
        self.TCombobox1.configure(textvariable=i)
        

        self.Button1 = tk.Button(top,command=Find)
        self.Button1.place(relx=0.344, rely=0.718, height=74, width=187)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#800040")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Product Sans} -size 28 -weight normal" )
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Find''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.143, rely=0.045, height=81, width=514)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Product Sans} -size 24 -weight normal")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Find to Improve Recognition''')


        top.mainloop()


