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
#Importation de tout les modules Tkinter répétition de certain pour évité les bugs

import os #Imporation de l'OS

def affichage(): #Cette fonction se charge de l'affichage avec Tkinter
    print()

def savoir(r, nbr_liste_1, nbr_liste_2):
    liste=[] #defini une liste
    for i in fe.split():#defini combient de lettre il y a dans le mot
        if len(i)>=nbr_liste_1:#compte le nombre de lettre et regarde si c'est au dessus du premier nombre
            if len(i)<=nbr_liste_2:#compte le nombre de lettre et regarde si c'est en dessous du premier nombre
                liste.append(i)#met dans la liste seuleument les mot comprie dans la fouchette en fonction de la difficulté
    return liste #retourne

def difficulté_high(val): #Pour établir l'interval de lettre des mot en fonction des difficultés sur la valeur basse
    if val==1:            #Si la valeur cliquer dans le menu tkinter est facile alors
        nbr_liste_2=4     #le nombre max de lettre est de
        return nbr_liste_2
    if val==2:#Si la valeur cliquer dans le menu tkinter est normal alors
        nbr_liste_2=8# le nombre max de lettre est de
        return nbr_liste_2
    if val==3:#Si la valeur cliquer dans le menu tkinter est difficile alors
        nbr_liste_2=100# le nombre max de lettre est de
        return nbr_liste_2

def difficulté_low(val): #Pour établir l'interval de lettre des mot en fonction des difficultés sur la valeur basse
    if val==1:#Si la valeur cliquer dans le menu tkinter est facile alors
        nbr_liste_1=1# le nombre min de lettre est de
        return nbr_liste_1
    if val==2:#Si la valeur cliquer dans le menu tkinter est normal alors
        nbr_liste_1=5# le nombre min de lettre est de
        return nbr_liste_1
    if val==3:#Si la valeur cliquer dans le menu tkinter est difficile alors
        nbr_liste_1=9# le nombre min de lettre est de
        return nbr_liste_1

def val_tentatives():
    global val
    if val==1:
        return val
    if val==2:
        return val
    if val==3:
        return val

OptionList = [ #Liste des difficultés pour l'affichage avec tkinter
        "Facile",
        "Normal",
        "Difficile"
        ] 

fenetre = Tk() #Defini la fonction tk en fenètre pour une meilleur compréantion

fenetre.geometry('350x100') #Taille de la fenètre

variable = tk.StringVar(fenetre) #Mise d'une fonction dans un seul mot pour simplifié l'écriture
variable.set(OptionList[0]) #Valeur par default du menu déroulent

opt = tk.OptionMenu(fenetre, variable, *OptionList) #Mise en option
opt.config(width=90, font=('Helvetica', 12)) #Mise en forme de la page Tkinter
opt.pack(side="top")#Mise en forme de la page Tkinter

labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')#Defini le font de callback
labelTest.pack(side="top")#defini le pack Tkinter

def callback(*args):#Quand un menu est selectionné dans Tkinter il l'affiche directement sur la page Tkinter
    labelTest.configure(text="Le menu seléctionné est : {}".format(variable.get(), bg='#f0f0f0'))

def show():#permet de mettre en variable le menu selectionné par l'utilisateur via le menu Tkinter
    label.config( text = clicked.get())
def close_window():#permet de fermer la fenètre
    fenetre.destroy()

variable.trace("w", callback)#permet de faire le lien entre la fenètre et les variable du programme

button = tk.Button( fenetre , text = "Valider", command = close_window ).pack() #bouton validé qui permet de fermer le fenètre toute en gardant la selection de l'utilisateur

fenetre.mainloop() #lance la fenètre

menu=variable.get()#permet de mettre dans la variable menu la difficulté recuperer par Show()
    
if menu=="Facile": #defini les diférante variable en fonction des fifficulté choisie
    menu=1
    val=1
if menu=="Normal":
    menu=2
    val=2
if menu=="Difficile":
    menu=3
    val=3

f=open("dico.txt", 'rb')#ouvre le dico en mode "read"
fe=f.read().decode("utf-8")#decode le dico avec l'UTF-8

#print(savoir(fe,difficulté_low(val), difficulté_high(val)))
