from tkinter import *
from tkinter import ttk
from PIL import Image

import api

class app():
    
    def __init__(self,master=None):
        
        #Primeiro container (Titulo e pesquisa)
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.labelTitle = Label(self.widget1,text='Previsão do tempo',font=('Arial',18))
        self.labelTitle.pack()
        self.EntryInputLocal = Entry(self.widget1,width=50)
        self.EntryInputLocal.pack(pady=10,side=LEFT)
        self.EntryInputLocal.insert(0,'Insira o nome para pesquisa')
        self.EntryInputLocal.config(foreground='#adadac')
        self.lupaPesquisa = PhotoImage(file='img/lupa.png')
        self.searchButton = Button(self.widget1,image=self.lupaPesquisa,bg='#0394fc')
        self.searchButton.pack(pady=10,side=RIGHT)
        self.searchButton.image = self.lupaPesquisa
        
        #Segundo container (Nome e temperatura da cidade)
        self.widget2 = Frame(master)
        self.widget2.pack()
        self.labelCidade = Label(self.widget2,text=api.nomeCidade,font=('Arial',14))
        self.labelCidade.pack(pady=20)
        self.labelTemperatura = Label(self.widget2,text=round(api.temperaturaAtual,1))
        self.labelTemperatura.pack(side=BOTTOM,pady=10)
        self.labelSimboloTemperatura = Label(self.widget2,text='°C')
        self.labelSimboloTemperatura.pack()
        
        
        #Terceiro container (Informações adicionais de temperatura)
        
        self.widget3 = Frame(master)
        self.widget3.pack()
        self.labelCondicao = Label(self.widget3,text=api.clima)
        self.labelCondicao.pack(side=LEFT,pady=10)
        self.labelIconCondicao = Label(self.widget3,image=api.iconeTemperatura)
        self.labelIconCondicao.pack(side=RIGHT,pady=10)
        
        #Quarto container (Informações adicionais (umidade/sensação termica))
        
        self.widget4 = Frame(master)
        self.widget4.pack()
        self.labelUmidade = Label(self.widget4,text=api.umidade)
        self.labelUmidade.pack(side=LEFT,padx=20,pady=10)
        self.labelSensacao = Label(self.widget4,text=api.sensacaoTermica)
        self.labelSensacao.pack(side=RIGHT,padx= 20,pady=10)
        
        


root = Tk()
root.config(background='#121212')
root.geometry('700x350')
app(root)
root.mainloop()
