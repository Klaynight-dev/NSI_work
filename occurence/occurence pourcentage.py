def search(liste, indice):
    occurence=0
    for i in range(len(liste)):
        if liste[i]==indice:
            occurence+=1
            pourcentage=occurence/len(liste)
            pourcentage*=100
    return pourcentage

liste=[1,2,4,5,7,8,9,9,9,10,12,13,15,19,20,22]

print(f"{search(liste,9)}%")

