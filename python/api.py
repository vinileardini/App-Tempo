import requests

import main

cidade = main.inputcidade

key = '1891b5e89c7c2a8d587345d6d22367b7'
request = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&lang=pt_br')
info = request.json()
    
nomeCidade = info['name']
pais = info['sys']['country']
umidade = info['main']['humidity']
temperaturaAtual = info['main']['temp']
sensacaoTermica = info['main']['feels_like']
clima =  info['weather'][0]['description']
iconeTemperatura = info['weather'][0]['icon']
    
    
    
    
    
    
    

    
