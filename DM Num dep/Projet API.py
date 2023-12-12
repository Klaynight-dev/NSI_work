import requests
import csv

# Remplacez "<VOTRE_CLE_API>" par votre clé d'API réelle
api_key = "<VOTRE_CLE_API>"

# Adresse que vous souhaitez géocoder
adresse_a_geocoder = "Saint-Brieuc"

# URL de l'endpoint de géocodage
url = f"https://api-adresse.data.gouv.fr/search/?q={adresse_a_geocoder}"

# Effectuer la requête HTTP GET
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Analyser la réponse JSON
    data = response.json()
    
    # Extraire les coordonnées géographiques de la première réponse
    if data["features"]:
        coordinates = data["features"][0]["geometry"]["coordinates"]
        latitude, longitude = coordinates[1], coordinates[0]
        print(f"Coordonnées géographiques de l'adresse '{adresse_a_geocoder}':")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    else:
        print("Aucun résultat trouvé pour cette adresse.")
else:
    print("La requête a échoué avec le code d'état:", response.status_code)



