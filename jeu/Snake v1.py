import pygame
import random

# Initialisation de pygame
pygame.init()

# Paramètres du jeu
largeur_fenetre = 640
hauteur_fenetre = 480
taille_case = 20
vitesse = 15

# Couleurs
couleur_fond = (0, 0, 0)
couleur_serpent = (0, 255, 0)
couleur_pomme = (255, 0, 0)

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Snake")

# Initialisation du serpent
serpent = [(200, 50), (210, 50), (220, 50)]
direction = "DROITE"

# Position de la pomme
pomme = (random.randrange(1, (largeur_fenetre // taille_case)) * taille_case,
         random.randrange(1, (hauteur_fenetre // taille_case)) * taille_case)

# Fonction pour afficher le serpent
def afficher_serpent(serpent):
    for segment in serpent:
        pygame.draw.rect(fenetre, couleur_serpent, pygame.Rect(segment[0], segment[1], taille_case, taille_case))

# Boucle de jeu
en_jeu = True
clock = pygame.time.Clock()

while en_jeu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_jeu = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "DROITE":
                direction = "GAUCHE"
            elif event.key == pygame.K_RIGHT and direction != "GAUCHE":
                direction = "DROITE"
            elif event.key == pygame.K_UP and direction != "BAS":
                direction = "HAUT"
            elif event.key == pygame.K_DOWN and direction != "HAUT":
                direction = "BAS"

    # Déplacement du serpent
    tete = list(serpent[0])
    if direction == "DROITE":
        tete[0] += taille_case
    elif direction == "GAUCHE":
        tete[0] -= taille_case
    elif direction == "HAUT":
        tete[1] -= taille_case
    elif direction == "BAS":
        tete[1] += taille_case

    serpent.insert(0, tuple(tete))

    # Gestion de la collision avec la pomme
    if serpent[0] == pomme:
        pomme = (random.randrange(1, (largeur_fenetre // taille_case)) * taille_case,
                 random.randrange(1, (hauteur_fenetre // taille_case)) * taille_case)
    else:
        serpent.pop()

    # Gestion de la collision avec les bords de l'écran
    if (serpent[0][0] < 0 or serpent[0][0] >= largeur_fenetre or
        serpent[0][1] < 0 or serpent[0][1] >= hauteur_fenetre):
        en_jeu = False

    # Gestion de la collision avec soi-même
    if serpent[0] in serpent[1:]:
        en_jeu = False

    # Rafraîchissement de l'écran
    fenetre.fill(couleur_fond)
    afficher_serpent(serpent)
    pygame.draw.rect(fenetre, couleur_pomme, pygame.Rect(pomme[0], pomme[1], taille_case, taille_case))
    pygame.display.flip()

    # Contrôle de la vitesse
    clock.tick(vitesse)

# Quitter pygame
pygame.quit()