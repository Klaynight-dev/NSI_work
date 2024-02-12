import csv
from collections import defaultdict

nom_fichier = 'dense.csv'
dico = defaultdict(str)

try:
    with open(nom_fichier, newline='') as csvfile:
        lecteur_csv = csv.reader(csvfile)
        index = 0
        for ligne in lecteur_csv:
            for item in ligne:
                dico[index] += str(item) + ','
            index += 1
    with open('dico.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in dico.items():
            writer.writerow([key, value])

    print(f"Le dictionnaire a été enregistré sous le nom 'dico.csv'.")
except FileNotFoundError:
    print(f"Le fichier '{nom_fichier}' n'a pas été trouvé.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
