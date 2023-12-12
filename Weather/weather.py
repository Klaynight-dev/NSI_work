import requests

api_key = '2dbcf398107ead0a716a4773269a7b68'

url = 'https://api.openweathermap.org/data/2.5/weather'
ville=input('Quelle ville voulez-vous ? : ')
params = {
    'q': ville,
    'units': 'metric',
    'lang': 'fr',
    'appid': api_key
}


response = requests.get(url, params=params)
data='none'

if response.status_code == 200:
    data = response.json()
    print(f"Données météorologiques actuelles pour {ville}:")
    print(f"Temps : {data['weather'][0]['description']}")
    print(f"Température : {data['main']['temp']}°C")
    print(f"Pression atmosphérique : {data['main']['pressure']} hPa")
    print(f"Humidité : {data['main']['humidity']}%")
    print(f"Vitesse de vent : {data['wind']['speed']}m/s")
    print(f"Longitude : {data['coord']['lon']}")
    print(f"Latitude : {data['coord']['lat']}")
else:
    print("La requête a échoué avec le code d'état :", response.status_code)
