import requests
import matplotlib.pyplot as plt
from datetime import datetime

api_key = '2dbcf398107ead0a716a4773269a7b68'

url = 'https://api.openweathermap.org/data/2.5/onecall'
ville = input('Quelle ville voulez-vous ? : ')
params = {
    'q': ville,
    'units': 'metric',
    'lang': 'fr',
    'exclude': 'current,minutely,daily',  # Exclure les données inutiles
    'appid': api_key
}

response = requests.get(url, params=params)
data = 'none'

if response.status_code == 200:
    data = response.json()
    hourly_data = data['hourly']  # Données horaires
    temps = [datetime.utcfromtimestamp(entry['dt']).strftime('%H:%M') for entry in hourly_data]
    temperatures = [entry['temp'] for entry in hourly_data]

    # Créer un graphique de la température en fonction de l'heure
    plt.figure(figsize=(10, 5))
    plt.plot(temps, temperatures, marker='o', linestyle='-', color='b')
    plt.title(f"Évolution de la température pour {ville}")
    plt.xlabel('Heure')
    plt.ylabel('Température (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)

    plt.show()
else:
    print("La requête a échoué avec le code d'état :", response.status_code)
