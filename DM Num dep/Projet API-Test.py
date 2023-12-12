import requests
import webbrowser
import folium
import csv
import numpy as np

def donnee():
    with open('prefectures.csv', 'r') as f:
        donnees= list(csv.reader(f, delimiter=";"))
        donnees = np.array(donnees)
    return donnees

donnees=donnee()

# Numéro du département que vous souhaitez interroger
code_departement = input("Entrer le département recherché : ")

# URL de l'endpoint des limites administratives
url_Dep = f"https://geo.api.gouv.fr/departements/{code_departement}?fields=codeRegion"

# Effectuer la requête HTTP GET
response = requests.get(url_Dep)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Analyser la réponse JSON
    data = response.json()
    codeR=data['codeRegion']
    
    urlReg = f"https://geo.api.gouv.fr/regions/{codeR}/departements?fields=nom"
    response=requests.get(urlReg)
    
    if response.status_code == 200:
        data=response.json()
        print(data)
        for clé in data:
            print(clé['nom'], clé['code'])
            
    else:
        print("La requête a échoué avec le code d'état:", response.status_code)

else:
    print("La requête a échoué avec le code d'état:", response.status_code)


# Coordonnées géographiques de la ville (à partir de la réponse JSON de l'API OpenWeatherMap)
for i in range(len(donnees)):
    if code_departement==donnees[i][0]:
        latitude = donnees[i][4]
        longitude = donnees[i][5]


# Créez une carte centrée sur la ville
m = folium.Map(location=[latitude, longitude], zoom_start=10)

# Ajoutez un marqueur à la position de la ville
folium.Marker([latitude, longitude], tooltip='Paris').add_to(m)

# Enregistrez la carte au format HTML (ou utilisez m.save("carte.html") pour enregistrer dans un fichier)
m.save('carte.html')

# Ouvrez la carte dans votre navigateur par défaut

webbrowser.open('carte.html')
    
