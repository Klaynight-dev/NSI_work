import subprocess
import requests
import folium

# Adresse IP ou nom de domaine de destination
destination = "www.toutatice.fr"

# Exécutez la commande tracert en utilisant subprocess
command = ["tracert", destination]
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Capturez la sortie standard et les erreurs
stdout, stderr = process.communicate()

# Créez une carte Folium
m = folium.Map(location=[0, 0], zoom_start=2)

# Parcourez la sortie de tracert pour récupérer les adresses IP
ip_addresses = []
lines = stdout.split("\n")
for line in lines:
    if "ms" in line:  # Les lignes avec "ms" contiennent les adresses IP
        parts = line.split()
        if len(parts) >= 4:
            ip_address = parts[3]
            ip_addresses.append(ip_address)

# Utilisez l'API IPinfo.io pour obtenir des informations géographiques et ajoutez-les à la carte Folium
for ip in ip_addresses:
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    data = response.json()
    location = data.get("loc")
    city = data.get("city", "N/A")
    country = data.get("country", "N/A")
    print(f"IP: {ip}, Location: {location}, City: {city}, Country: {country}")

    if location:
        lat, lon = location.split(",")
        folium.Marker(
            location=[float(lat), float(lon)],
            popup=f"IP: {ip}<br>City: {city}<br>Country: {country}",
        ).add_to(m)

# Enregistrez la carte dans un fichier HTML
map_file = "traceroute_map.html"
m.save(map_file)

# Ouvrez la carte dans le navigateur par défaut
import webbrowser
webbrowser.open(map_file)
