import csv

# Ouvrir le fichier CSV avec un encodage spécifique (par exemple, iso-8859-1)
with open('prefectures.csv', mode='r', encoding='iso-8859-1') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv)

    # Lire la première ligne du fichier CSV pour obtenir les en-têtes
    entetes = next(lecteur_csv)

    # Parcourir chaque ligne du fichier CSV
    for ligne in lecteur_csv:
        # Votre logique de traitement des données ici
        print(ligne)

# Afficher les en-têtes
print(entetes)
# N'oubliez pas de fermer le fichier CSV après avoir terminé
fichier_csv.close()
