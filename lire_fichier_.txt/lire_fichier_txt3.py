import os

Fichier = open("dico.txt","rb")
contenu = Fichier.read().decode("utf-8")
print(type(contenu))
Fichier.close()
print(len(contenu))
#---------------#------------------------------------
val=contenu.split()[3]

print(f"voici le 3éme mot du dictionnaire:  {val}")

val=contenu.split()[:3]
print(f"voici les trois premiers mots du dictionnaire: {val}")

val=contenu.split()[-3:]
print(f"voici les trois derniers mots du dictionnaire: {val}")
# #---------------#------------------------------------

file = open("monfichier.txt", "w") 
file.write("Voici le texte de mon fichier") 
file.close()


















