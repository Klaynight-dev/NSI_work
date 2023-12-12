from random import *
from math import *
from turtle import *
from random import *
import sys
from colorama import *
import time

#===============================================def=======================================================================================================================================================

def jdlc():
    jdlcp=randint(1,20)
    print("Bonjour, vous êtes l'heureux candidat au ...")
    print("Jeu De La Chance ! veuillez m'indiquer un nombre compris entre 1 et 20, si vous êtes proche de 5 unité ou moins vous aurai le droit à une second chance ! Alors bon courage et commançons le jeu!")
    gd=0
    while gd==1:
        rslt=int(input("Veuillez enter un nombre compris entre 1 et 20"))
        if rslt==jdlcp:
            print("Bravo, tu as gagner une magnifique sonbtueuse que dis-je exeptionnel banane !")
            gd=1
        elif rslt>= jdlcp-5 and rslt<=jdlcp+5:
            print("Arg, mince c'est bien essayer mais il y à un écard de 5 ou moins entre votre réponse est la bonne réponse. reessiller encore")

stream = AnsiToWin32(sys.stderr).stream

cont=False
while cont==False:
    menu=int(input("Quelle menu voulez vous ? : "))
    w=2
    
#=====================================================1===================================================================================================================================================

    if menu==1:
        nb_annees=2
        nb_secondes=3600*24*365*nb_annees
        print("Dans",  nb_annees, "annees de 365 jours, il y a ", nb_secondes, "secondes.")

    # Les deux codes sont identique mais differrament codé
    
#=====================================================2===================================================================================================================================================

    if menu==2:
        nb_annees=2
        nb_secondes=3600*24*365*nb_annees
        print(f"Dans {nb_annees} annees de 365 jours, il y a {nb_secondes} secondes.")

#=====================================================3===================================================================================================================================================

    if menu==3:
        bb=1237
        pbb=12

        bbdp=bb//pbb
        rbb=bb%pbb

        #bb = bonbon / pbb = paquet bonbon / bbdp = bonbon dans paquet / rbb = reste bonbon

        print(f"Nous avons {bbdp} bonbons répartie dans {pbb} paquet ! Malheureusement il nous reste {rbb} bonbon(s) qui ne peut(vent) être répartie dans les paquets.")

#=====================================================4===================================================================================================================================================

    if menu==4:
        longueur=5
        largeur=3
        aire=longueur*largeur
        print(aire)

#=====================================================5===================================================================================================================================================

    if menu==5:
        p=23 #Prix
        p=p+1/10*p
        print(f"Avec une hausse de 10% le prix de notre produit est maintenant de {p}€")

#=====================================================6===================================================================================================================================================

    if menu==6:
        a=8
        b=12
        c=a
        a=b
        b=c
        print(f"a={a} b={b}")

#=====================================================7===================================================================================================================================================

    if menu==7:
        a=2
        print(type(a))
        b=2.894
        print(type(b))
        c="Bonjour !"
        print(type(c))
        L=[2, "Youpi", 23.5, 9]
        print(type(L))

#=====================================================8===================================================================================================================================================

    if menu==8:
        carre=float(input("Rentrez une côte : "))
        print("La surface du carré est de :", carre*carre)

#=====================================================9===================================================================================================================================================

    if menu==9:
        aleatoire=randint(1,100)
        while aleatoire!=0:
            print(f"Voici le nombre aléatoire choisi: {aleatoire}")
            aleatoire=rd.randint(1,100)

#=====================================================10===================================================================================================================================================

    if menu==10:
        a=True
        b=False
        print(type(a))
        print(type(b))

#=====================================================11===================================================================================================================================================

    if menu==11:
        n = int(input("Entrez un nombre : "))
        if (n % 2) == 0:
           print("{0} est Paire".format(n))
        else:
           print("{0} est Impaire".format(n))

#=====================================================12===================================================================================================================================================

    if menu==12:
        if1=input("Quelle est votre Nom : ")
        if2=input("Quelle est votre Prenom : ")
        if3=float(input("Quelle est votre note de BAC : "))
        
        if if3>=14 and if3<16:
            mention="asser bien"
        elif if3>=16 and if3<18:
            mention="bien"
        elif if3>=18:
            mention="très bien"
        
        if if3<=8:
            print(f"Bonjour {if2} {if1}, vous été Refuser avec une moyenne de {if3}")
        elif if3>=8 and if3<10:
            print(f"Bonjour {if2} {if1}, vous être Admis au Rattrapage avec une moyenne de {if3}")
        elif if3>=10 and if3<14:
            print(f"Bonjour {if2} {if1}, vous être Admis avec une moyenne de {if3}")
        elif if3>=14:
            print(f"Bonjour {if2} {if1}, vous être Admis avec la mention {mention} votre moyenne est de {if3}")

#=====================================================13===================================================================================================================================================

    if menu==13:
        nmbr=int(input("Veuillez sésir un nombre entier : "))
        n1=1
        n2=int(input("Quelle quantité de table voulez vous ? : "))
        for i in range(n2):
            print(nmbr, "x", n1, "=", nmbr*n1)
            n1=n1+1


    if menu==14:
        print("In Development")
#==============================================End=Script================================================================================================================================================

    if menu>=14:
        print(Fore.RED +"ERROR 404 : Ce menu est introuvable !"+Fore.RESET, file=stream)
    
    while w==2 :
        rep=input("Voulez vous rester le programme ? : ")
        
        if rep=="non":
            cont=True
            w=1
            time.sleep(1)
            print("Fermeture du programme en cour.")
            time.sleep(1)
            print("Fermeture du programme en cour..")
            time.sleep(1)
            print("Fermeture du programme en cour...")

    
        elif rep=="oui":
            w=1
            cont=False

        else:
            print(Fore.RED +"ERROR 404 : Valeur non trouver !"+Fore.RESET, file=stream)
            w=2
