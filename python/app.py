from tkinter import *
from tkinter import ttk
from PIL import Image

import sys
import os

class app():
    
    def __init__(self,master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.labelTitle = Label(self.widget1,text='Previsão do tempo')
        self.labelTitle.pack()
        self.EntryInputLocal = Entry(self.widget1,width=50)
        self.EntryInputLocal.pack(pady=10,side=LEFT)
        self.lupaPesquisa = PhotoImage('img/lupa_r.png')
        self.searchButton = Button(self.widget1,image=self.lupaPesquisa)
        self.searchButton.pack(pady=10,side=RIGHT)
        self.searchButton.image = self.lupaPesquisa
        


root = Tk()
root.geometry('700x350')
app(root)
root.mainloop()
