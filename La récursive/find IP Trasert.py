import requests
import folium

def afficher_localisation_ip(adresse_ip):
    # Obtenir les informations de localisation à partir de l'adresse IP en utilisant ipinfo.io
    url = f"http://ipinfo.io/{adresse_ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Récupérer les coordonnées de latitude et longitude
        if 'loc' in data:
            latitude, longitude = data['loc'].split(',')
            # Créer une carte à l'aide de folium et ajouter un marqueur à la position trouvée
            carte = folium.Map(location=[float(latitude), float(longitude)], zoom_start=10)
            folium.Marker([float(latitude), float(longitude)], popup=f"Localisation IP: {adresse_ip}").add_to(carte)
            # Afficher la carte dans un navigateur ou un fichier HTML
            carte.save("localisation_ip.html")
            print("La localisation a été affichée sur la carte dans le fichier localisation_ip.html")
        else:
            print("Impossible de récupérer les coordonnées de localisation pour cette adresse IP.")
    else:
        print("Erreur lors de la requête vers l'API.")

# Utilisation de la fonction avec une adresse IP
adresse_ip_a_afficher = "185.233.130.14"  # Mettez ici l'adresse IP que vous souhaitez rechercher
afficher_localisation_ip(adresse_ip_a_afficher)
