import requests

def consomeAPI(cidade):
    key = '1891b5e89c7c2a8d587345d6d22367b7'
    request = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&lang=pt_br')
    print(request.json())
    
