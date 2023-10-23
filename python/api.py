import requests
from urllib.request import urlopen
import main
from PIL import Image,ImageTk

        
cidade = main.inputCidade

arquivo = open(r'C:\Users\Vinícius\Documents\openweatherAPI.txt','r',encoding='utf-8')
key = arquivo.readline()

request = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&lang=pt_br')
info = request.json()
    
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


        
    



    
    
    
    
    
    

    
