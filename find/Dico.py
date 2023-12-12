# def maxdico(likes):
#     maxi=likes["Bob"]
#     for i in likes:
#         if likes[i]>maxi:
#             maxi=likes[i]
#     return maxi
# 
# likes={'Bob':102,'Ada':201,'Alice':103,'Tim':50}
# 
# print(maxdico(likes))
def moyen(resultats, nom):
    b=0
    coef=0
    for noms in resultats:
        if nom==noms:
            for exam, notes in resultats[noms].items():
                a=notes[0]*notes[1]
                b+=a
                coef+=notes[1]
    return round(b/coef,2)

resultats={'Dupont':{
    'DS1':[15.5,4],
    'DM1':[14.5,1],
    'DS2':[13,4],
    'PROJET1':[16,3],
    'DS3':[14,4]
    },'Durant':{
    'DS1':[6,4],
    'DM1':[14.5,1],
    'DS2':[8,4],
    'PROJET1':[9,3],
    'IE1':[7,3],
    'DS3':[7,4],
    'DS4':[15,4]}}
print(moyen(resultats, 'Dupont'))