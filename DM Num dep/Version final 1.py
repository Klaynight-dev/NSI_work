import requests
import webbrowser
import folium
import csv
import numpy as np

def import_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("La requête a échoué avec le code d'état:", response.status_code)
        return None

def load_data_from_csv(file_path):
    with open(file_path, 'r') as f:
        return np.array(list(csv.reader(f, delimiter=";")))

def create_map():
    return folium.Map(location=[46.227638, 2.213749], zoom_start=6)

def main():
    donnees = load_data_from_csv('prefectures.csv')
    code_departement = input("Entrer le département recherché : ")

    url_Dep = f"https://geo.api.gouv.fr/departements/{code_departement}?fields=codeRegion"
    data = import_data(url_Dep)
    
    if data is None:
        return
    
    codeR = data['codeRegion']
    print(data)
    nom_dep_prime = data['nom']
    
    url_Reg = f"https://geo.api.gouv.fr/regions/{codeR}/departements?fields=nom"
    data = import_data(url_Reg)
    print(data)

    m = create_map()

    for trouver in data:
        num_dep = trouver['code']
        nom_dep = trouver['nom']
        
        for i in range(len(donnees)):
            if num_dep == donnees[i][0]:
                print(donnees[i][4])
                print(donnees[i][5])
                nom_pref = donnees[i][2]
                latitude = donnees[i][4]
                longitude = donnees[i][5]

        a = f"{nom_pref} {nom_dep} {num_dep}"
        
        couleur = 'black' if code_departement == num_dep else 'blue'
        
        folium.Marker([latitude, longitude], tooltip=nom_pref, icon=folium.Icon(color=couleur), popup=a).add_to(m)

    m.save('carte.html')
    webbrowser.open('carte.html')

if __name__ == "__main__":
    main()
