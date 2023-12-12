from random import *
from math import *
from random import *
import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter as Label
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import tkinter as Label

import os

def affichage():
    print()

def savoir(r, nbr_liste_1, nbr_liste_2):
    liste = []
    for i in fe.split():
        if len(i) >= nbr_liste_1:
            if len(i) <= nbr_liste_2:
                liste.append(i)
    return liste

def difficulte_high(val):
    if val == 1:
        nbr_liste_2 = 4
        return nbr_liste_2
    if val == 2:
        nbr_liste_2 = 8
        return nbr_liste_2
    if val == 3:
        nbr_liste_2 = 100
        return nbr_liste_2

def difficulte_low(val):
    if val == 1:
        nbr_liste_1 = 1
        return nbr_liste_1
    if val == 2:
        nbr_liste_1 = 5
        return nbr_liste_1
    if val == 3:
        nbr_liste_1 = 9
        return nbr_liste_1

def val_tentatives():
    global val
    if val == 1:
        return val
    if val == 2:
        return val
    if val == 3:
        return val

OptionList = [
    "Facile",
    "Normal",
    "Difficile"
]

fenetre = Tk()
fenetre.geometry('350x100')

variable = tk.StringVar(fenetre)
variable.set(OptionList[0])

opt = tk.OptionMenu(fenetre, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack(side="top")

labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

def callback(*args):
    labelTest.configure(text="Le menu sélectionné est : {}".format(variable.get(), bg='#f0f0f0'))

def show():
    label.config( text = clicked.get())
def close_window():
    fenetre.destroy()

variable.trace("w", callback)

button = tk.Button(fenetre , text = "Valider", command = close_window).pack()

fenetre.mainloop()

menu = variable.get()

if menu == "Facile":
    menu = 1
    val = 1
if menu == "Normal":
    menu = 2
    val = 2
if menu == "Difficile":
    menu = 3
    val = 3

f = open("dico.txt", 'rb')
fe = f.read().decode("utf-8")

# Ici, vous devrez intégrer ces fonctions et variables dans votre jeu du Pendu.

def get_random_word(difficulty):
    # Implémentez cette fonction pour obtenir un mot au hasard en fonction de la difficulté
    pass

def play_game():
    global repetition
    solution = get_random_word(val)
    tentatives = 0
    apparetre1 = 0
    apparetre2 = 0
    apparetre3 = 0
    apparetre4 = 0
    apparetre5 = 0
    apparetre6 = 0
    Lettre_fausse = []

    def lettrefausse(proposition, Lettre_fausse):
        if proposition not in Lettre_fausse:
            Lettre_fausse.append(proposition)

    def Tentapp(val_tentatives):
        global tentatives, apparetre1, apparetre2, apparetre3, apparetre4, apparetre5, apparetre6
        if val_tentatives == 1:
            tentatives = 28
            apparetre1 = 4
            apparetre2 = 8
            apparetre3 = 12
            apparetre4 = 16
            apparetre5 = 20
            apparetre6 = 24
        elif val_tentatives == 2:
            tentatives = 14
            apparetre1 = 2
            apparetre2 = 4
            apparetre3 = 6
            apparetre4 = 8
            apparetre5 = 10
            apparetre6 = 12
        elif val_tentatives == 3:
            tentatives = 14
            apparetre1 = 2
            apparetre2 = 4
            apparetre3 = 6
            apparetre4 = 8
            apparetre5 = 10
            apparetre6 = 12

    # Mettez le reste de la logique du jeu ici
    # Vous devrez ajouter le code pour le jeu du Pendu ici

    # Affichez une boîte de dialogue demandant si l'utilisateur souhaite rejouer
    if askyesno("Programme by Elouan", "Voulez-vous rejouer ?"):
        repetition = 1
    else:
        repetition = 0

# Créez un bouton pour commencer le jeu
start_button = tk.Button(fenetre, text="Commencer le jeu", command=play_game)
start_button.pack()
fenetre.mainloop()

print("Merci d'avoir joué !")
print("À bientôt !")
