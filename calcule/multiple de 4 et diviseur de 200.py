def est_multiple_de_4_et_diviseur_de_200():
    liste=[]
    for nombre in range(1000):
        if nombre % 6 == 0 and nombre % 200 == 0:
            liste.append(i)
    return liste
        
print(est_multiple_de_4_et_diviseur_de_200())
