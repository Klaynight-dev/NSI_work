import os

Fichier = open("jardin des plantesV1.txt","rb")
contenu = Fichier.read().decode("utf-8")
print(contenu)
Fichier.close()

print("")

print(len(contenu))

print("")

#---------------#------------------------------------
val=contenu.split()[7]
print(f"Voici l'impression de val:  {val}")

#---------------#------------------------------------

file = open("monfichier.txt", "w") 

file.write("Bonjour je vous informe que vous êtes nul")
file.close()

print("")

file = open("monfichier.txt", "rb") 
cont2 = file.read().decode("utf-8")
print(cont2)
file.close()
