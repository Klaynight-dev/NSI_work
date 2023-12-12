from random import *
        
def affichage():
    verif=False
            
    while verif==False:
        affi=input("Voulez vous l'affichiage ? : ")

        if affi=="oui":
             verif==True
             affichange=1
             return(affichange)
         
        elif affi=="non":
             verif==True
             affichange=2
             return 2
         
        else:
            print(Fore.RED +"ERROR 404 : Valeur non trouver !"+Fore.RESET, file=stream)
            verif=False
        
np=input("Quelle est votre prénom ? : ")
butin=int(input("choississez un nombre : "))
butinin=butin
Total=0
er=int(input("Quel est le 1er décisif ? : "))
eme=int(input("Quel est le 2eme décisif ? : "))
  
affichange=affichage()
while butin>0:
    butin=butin-randint(er,eme)
    if butin<0:
        if affichange==1:
            print("Le butin est vide !")
            Total=Total+1
        elif affichange==2:
            Total=Total+1
    else:
        if affichange==1:
            print(butin, end=",")
        Total=Total+1
Moyenne = format(butinin/Total, "#.2f")
print (f"Ca y est {np}, le jeu est terminé ! Il y a eu {Total} tour au total pour terminer. Avec comme nombre décisif '{er}' et '{eme}'. En moyenne il y a eu '{Moyenne}' dans ce lancement de dés !")