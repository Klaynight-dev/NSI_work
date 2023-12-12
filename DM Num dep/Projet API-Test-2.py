import requests
import webbrowser
import folium
import csv
import numpy as np

#==================================================================================================#
def import_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Analyser la réponse JSON
        data = response.json()
    else:
        print("La requête a échoué avec le code d'état:", response.status_code)
    return data

def donnee():
    with open('prefectures.csv', 'r') as f:
        donnees= list(csv.reader(f, delimiter=";"))
        donnees = np.array(donnees)
    return donnees

#==================================================================================================#

donnees=donnee()
code_departement = input("Entrer le département recherché : ")

url_Dep = f"https://geo.api.gouv.fr/departements/{code_departement}?fields=codeRegion"
data=import_data(url_Dep)
codeR=data['codeRegion']
print(data)
nom_dep_prime=data['nom']
url_Reg = f"https://geo.api.gouv.fr/regions/{codeR}/departements?fields=nom"
data=import_data(url_Reg)
print(data)

# Créez une carte centrée sur la ville
m = folium.Map(location=[46.227638, 2.213749], zoom_start=6)

for trouver in range(len(data)):
    num_dep=data[trouver]['code']
    nom_dep=data[trouver]['nom']
    for i in range(len(donnees)):
        if num_dep==donnees[i][0]:
            print(donnees[i][4])
            print(donnees[i][5])
            nom_pref=donnees[i][2]
            latitude = donnees[i][4]
            longitude = donnees[i][5]

    a=f"{nom_pref} {nom_dep} {num_dep}"
    
    if code_departement==num_dep:
        couleur='black'
    else:
        couleur='blue'
    
    # Ajoutez un marqueur à la position de la ville
    folium.Marker([latitude, longitude], tooltip=nom_pref, icon=folium.Icon(color=couleur), popup=a).add_to(m)

# Enregistrez la carte au format HTML (ou utilisez m.save("carte.html") pour enregistrer dans un fichier)
m.save('carte.html')

# Ouvrez la carte dans votre navigateur par défaut

webbrowser.open('carte.html')