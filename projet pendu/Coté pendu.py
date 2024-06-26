from random import *
from random import choice
from tkinter import *

from TP_Elouan_Passereau import *
#appel le programme de difficulté qui utilise Tkinter

import tkinter as tk
from tkinter.simpledialog import Dialog

class AskYesNo(Dialog):
    def __init__(self, title, message, parent=None):
        if not parent:
            parent = tk._default_root

        self.message = message
        Dialog.__init__(self, parent, title)

    def body(self, master):
        w = tk.Label(master, text=self.message, justify=tk.LEFT)
        w.grid(row=0, padx=5, sticky=tk.W)

    def buttonbox(self):
        """ajout d'une button box standard.

        Nous utilisons Oui et Non en texte
        """

        box = tk.Frame(self)

        w = tk.Button(box, text="Oui", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="Non", width=10, command=self.cancel)
        w.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    def apply(self):
        "If Oui was clicked"
        self.result = True

def askyesno(title, message):
    "Returns if the user clicked the Oui button."
    msg = AskYesNo(title=title, message=message)
    return msg.result is True

#défini si le joueur veux rejouer
def jouer():
    def quite():
        global repetition
        if askyesno("Programme by Elouan", "Voullez-vous rejouer ?"):
            repetition=1
            root.destroy()
        else:
            repetition=0
            root.destroy()
    root = tk.Tk()
    tk.Button(root, text="Ok", command=quite).grid(padx=50, pady=20)
    root.mainloop()

#Defini un mot au hasard
def _difficulty_():
    mot_nouveau=1                                                    #variable qui permet la boucle while
    while mot_nouveau==1:                                            #boucle
        choix = savoir(fe,difficulté_low(val), difficulté_high(val)) #la variable choix et attribué à savoir qui met dans un liste tout les mots qui ont entre ten et ten de lettre en fonction de la difficulté choisis.
        if choix not in mot_deja_prit:                               #savoir si le moi choisis au hazard à deja été prix dans une partie précédente
            mot_nouveau=0                                            #arrète la boucle
    return choix[randint(0, len(choix))]                             #retourne le mot avec ses lettre en liste

def lettrefausse(proposition, Lettre_fausse):
    if proposition not in Lettre_fausse:
        Lettre_fausse.append(proposition)

def tentatives():
    global tentatives
    
    global apparetre1
    global apparetre2
    global apparetre3
    global apparetre4
    global apparetre5
    global apparetre6
    
    if val_tentatives==1:
        tentatives=28
        apparetre1=4
        apparetre2=8
        apparetre3=12
        apparetre4=16
        apparetre5=20
        apparetre6=24
        
    elif val_tentatives==2:
        tentatives=14
        apparetre1=2
        apparetre2=4
        apparetre3=6
        apparetre4=8
        apparetre5=10
        apparetre6=12
    elif val_tentatives==3:
        tentatives=14
        apparetre1=2
        apparetre2=4
        apparetre3=6
        apparetre4=8
        apparetre5=10
        apparetre6=12
    
#====================================Variable=============================================================#

mot_deja_prit=[] #défini les mot déja utilisé dans les parties pressédente

repetition=1

#====================================Programme============================================================#

while repetition==1: #pour que la partie continue temps que l'utilisateur veux continué

    solution = _difficulty_() #defini la solution avec un seul mot
    tentatives = 0            #definition le nombre de tentative
    tentatives()
    apparetre1=0               #definition de l'intervale ou apparet le pendu
    apparetre2=0
    apparetre3=0
    apparetre4=0
    apparetre5=0
    apparetre6=0
    apparetre()
    affichage = ""            #sert pour l'affichage des '-' ou des lettres trouvés
    lettres_trouvees = ""     #sert à stocker les lettres trouver par l'utilisateur
    Lettre_fausse=[]
    tour=1
    
    for l in solution:
        affichage = affichage + "-"

    print("====>> Bienvenue dans le pendu <<=====")

    while tentatives > 0:
        print("\nMot à deviner : ", affichage)
        if tour>1:
            print(f"Voici les lettres déja proposé mais fausse : {Lettre_fausse}")
        proposition = input("proposez une lettre : ")[0:1].lower()

        if proposition in solution:
          lettres_trouvees = lettres_trouvees + proposition
          print("-> Bien vu!")
          tour+=1
          print(f"Il vous reste {tentatives} tentatives avant que le pendu soit terminé.")

          
        else:
            tentatives = tentatives - 1
            print("-> Nope\n")
            if tentatives==0:
                print(" ==========Y= ")
            if tentatives<=apparetre1:
                print(" ||/       |  ")
            if tentatives<=apparetre2:
                print(" ||        0  ")
            if tentatives<=apparetre3:
                print(" ||       /|\ ")
            if tentatives<=apparetre4:
                print(" ||       / \ ")
            if tentatives<=apparetre5:                    
                print("/||           ")
            if tentatives<=apparetre6:
                print("==============\n")
            if tentatives==0:
                print(f"Le mot été {solution}")
            lettrefausse(proposition, Lettre_fausse)
            tour+=1
            print(f"Il vous reste {tentatives} tentatives avant que le pendu soit terminé.")

        affichage = ""
        for x in solution:
          if x in lettres_trouvees:
              affichage += x + " "
          else:
              affichage += "_ "

        if "_" not in affichage:
          print(">>> Gagné! <<<")
          print(f"Le mot été {solution}")
          break
     
    print("\n    * Fin de la partie *    ")
    print("") #simple mise en forme
    
    jouer()

print("Merci d'avoir jouer !")
print("A bientôt !")