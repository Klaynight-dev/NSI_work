def search(liste, indice):
    taille=len(liste)
    for i in range(len(liste)):
        if liste[i]==indice:
            taille=i+1
    return taille

liste=[1,2,4,5,7,8,9,9,10,12,13,15,19,20,22,9]

print(search(liste, 9))