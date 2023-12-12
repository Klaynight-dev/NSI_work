from time import *
import numpy as np
import pygame
from pygame.locals import *
 
pygame.init()
 
NombreDePoule = 10
 
ClicDetection = {'Shop': False,'Machine': False}
 
def CreeDefautMenu():
    #Cree le menu de départ
     
    global fenetre, Background, Shop, Machine, Poule, FondPoule
     
    fenetre = pygame.display.set_mode((900,800))
 
    Background = pygame.image.load("FondNoir.jpg") 
    fenetre.blit(Background,(0,0))
 
    Shop = pygame.image.load("AlphaTextureShop.jpg")
    fenetre.blit(Shop,(200,200))   
     
    Machine = pygame.image.load("AlphaTextureMachine.jpg")
    fenetre.blit(Machine,(400,200))
 
    FondPoule = pygame.font.Font(None, 30)
    Poule = FondPoule.render("Poule: " + str(NombreDePoule),1,(255,255,255))
    fenetre.blit(Poule,(0,0))
 
def ApparaitreMenu():
    #Affiche inventaire du shop
     
    if ClicDetection['Shop'] == True:
         
        FontShop = pygame.image.load("FontShop.jpg")
        fenetre.blit(FontShop,(100,100))
     
        font = pygame.font.Font(None, 40)
        text = font.render("Acheter Des Poules",1,(10,10,10))
        fenetre.blit(text,(130,135))
        print(NombreDePoule)
     
    if ClicDetection['Machine'] == True:
         
        FontMachine = pygame.image.load("FontShop.jpg")
        fenetre.blit(FontMachine,(100,100))
             
    PlusOuMoins()  
     
def FermerPage():
    #Ferme les menus deja ouvert   
     
    global fenetre, Background, Shop, Machine, Poule
     
    #v Ferme Page v
    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] in range(730,780) and event.pos[1] in range(110,160):
     
        fenetre.blit(Background,(0,0))
        fenetre.blit(Shop,(200,200))
        fenetre.blit(Machine,(400,200))
        fenetre.blit(Poule,(0,0))
 
def DetecteCollision():
    #Detecte les collision
     
    global NombreDePoule
     
    #v Shop v
    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] in range(200,300) and event.pos[1] in range(200,300):
             
        ClicDetection['Shop'] = True
         
        ClicDetection['Machine'] = False
        ApparaitreMenu()
         
    #v Machine v
    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] in range(400,500) and event.pos[1] in range(200,300):
     
        ClicDetection['Machine'] = True
         
        ClicDetection['Shop'] = False
        ApparaitreMenu()   
 
    if event.type == MOUSEBUTTONDOWN and event.button == 1:
     
        print(event.pos[0],event.pos[1])
     
    FermerPage()
 
def PlusOuMoins():
    #Incremantion ou decremantion d'une variable
    global NombreDePoule
     
    if ClicDetection['Shop'] == True:
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] in range(130,400) and event.pos[1] in range(135,160):
             
            NombreDePoule = NombreDePoule + 1
 
def MiseAJour():
    #Met a jour
     
    FondPoule = pygame.font.Font(None, 30)
    Poule = FondPoule.render("Poule: " + str(NombreDePoule),1,(250,250,250))
 
CreeDefautMenu()   
while True:
    pygame.display.flip()
    MiseAJour()
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            PlusOuMoins()
            DetecteCollision()