def search(liste, indice):
    occurence=0
    for i in range(len(liste)):
        if liste[i]==indice:
            occurence+=1
    return occurence

liste=[1,2,4,5,7,8,9,9,10,12,13,15,19,20,22]

print(search(liste, 9))
