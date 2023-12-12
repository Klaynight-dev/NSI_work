# def doublon(liste):
#     for i in range(len(liste)-1):
#         if liste[i]==liste[i+1]:
#             return True
#     return False

def doublon(liste):
    dbl=False
    for i in range(len(liste)-1):
        if liste[i]==liste[i+1]:
            dbl=True
    return dbl


liste=[1,2,4,5,7,8,9,9,10,12,13,15,19,20,22]
liste2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(doublon(liste))