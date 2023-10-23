from tkinter import *
from tkinter import ttk
from PIL import Image
import tkinter as tk
import requests
from urllib.request import urlopen
from tkinter.commondialog import Dialog

import api


class app():
    
    def __init__(self,master=None):
        
        #Primeiro container (Titulo e pesquisa)
        self.widget1 = Frame(master,background='#121212')
        self.widget1.pack()
        self.labelTitle = Label(self.widget1,text='Previsão do tempo',font=('Arial',18),foreground='#f7f9fc',background='#121212')
        self.labelTitle.pack()
        self.EntryInputLocal = Entry(self.widget1,width=50)
        self.EntryInputLocal.pack(pady=10,side=LEFT)
        self.EntryInputLocal.insert(0,'Insira o nome para pesquisa')
        self.EntryInputLocal.config(foreground='#adadac',background='#121212')
        self.lupaPesquisa = PhotoImage(file='img/lupa.png')
        self.searchButton = Button(self.widget1,image=self.lupaPesquisa,bg='#0394fc',command=self.pesquisa)
        self.searchButton.pack(pady=10,side=RIGHT)
        self.searchButton.image = self.lupaPesquisa
        
        #Segundo container (Nome e temperatura da cidade)
        self.widget2 = Frame(master,background='#121212')
        self.widget2.pack()
        self.labelCidade = Label(self.widget2,text=api.nomeCidade,font=('Arial',14),foreground='#f7f9fc',background='#121212')
        self.labelCidade.pack(pady=20)
        self.labelTemperatura = Label(self.widget2,text=(round(api.temperaturaAtual,1),'°C'),foreground='#f7f9fc',background='#121212')
        self.labelTemperatura.pack(side=BOTTOM,pady=10)
        
        
        #Terceiro container (Informações adicionais de temperatura)
        
        self.widget3 = Frame(master,background='#121212')
        self.widget3.pack()
        self.labelCondicao = Label(self.widget3,text=api.clima)
        self.labelCondicao.config(foreground='#f7f9fc',background='#121212')
        self.labelCondicao.pack(side=LEFT,pady=10)
        self.iconLabel = tk.PhotoImage(data=api.iconeTemperatura)
        self.labelIconCondicao = Label(self.widget3,image=self.iconLabel,background='#121212')
        self.labelIconCondicao.image = self.iconLabel
        self.labelIconCondicao.pack(side=RIGHT,pady=10)
        
        #Quarto container (Informações adicionais (umidade/sensação termica))
        
        self.widget4 = Frame(master,background='#121212')
        self.widget4.pack()
        self.labelUmidade = Label(self.widget4,text=('Umidade:',api.umidade,'%'),foreground='#f7f9fc',background='#121212')
        self.labelUmidade.pack(side=LEFT,padx=20,pady=10)
        self.labelSensacao = Label(self.widget4,text=('Sensação térmica:', round(api.sensacaoTermica,1),'°C'),foreground='#f7f9fc',background='#121212')
        self.labelSensacao.pack(side=RIGHT,padx= 20,pady=10)
        
    
    def resetDefaultSearchText(self):
        
        self.EntryInputLocal.insert(1,'')
    
    def pesquisa(self):
        
        cidadePesquisa = self.EntryInputLocal.get()
        
        print(cidadePesquisa)

        arquivo = open(r'C:\Users\Vinícius\Documents\openweatherAPI.txt','r',encoding='utf-8')
        key = arquivo.readline()
        
        request = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cidadePesquisa}&appid={key}&lang=pt_br')
        info = request.json()
        
        print(info)
        
        nomeCidade = info['name']
        pais = info['sys']['country']
        umidade = info['main']['humidity']
        temperaturaAtual = info['main']['temp']-273
        sensacaoTermica = info['main']['feels_like']-273
        clima =  info['weather'][0]['description']
        valorIconeTemperatura = info['weather'][0]['icon']

        # Modificações para uso do ícone da temperatura
        urlIconeTemperatura = f'https://openweathermap.org/img/wn/{valorIconeTemperatura}.png'
        abreImagem = urlopen(urlIconeTemperatura)
        rawImagem = abreImagem.read()
        abreImagem.close()

        iconeTemperatura = rawImagem
        
        
        #Alterações para mostrar informações da cidade pesquisada
        
        
        
        self.labelCidade.config(text=(nomeCidade,',',pais))
        self.labelTemperatura.config(text=(round(temperaturaAtual,1),'°C'))
        self.labelCondicao.config(text=clima)
        self.labelSensacao.config(text=('Sensação térmica:',round(sensacaoTermica,1),'°C'))
        self.iconLabel = tk.PhotoImage(data=iconeTemperatura)
        self.labelIconCondicao.config(image=self.iconLabel)
        self.labelUmidade.config(text=('Umidade:',umidade,'%'))
        
            
                
        
        
        
        
        
        
        
        
        
        


root = Tk()
root.config(background='#121212')
root.minsize(700,350)
root.maxsize(700,350)
app(root)
root.mainloop()
