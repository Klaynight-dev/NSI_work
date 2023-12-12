import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définir les dimensions de l'écran
largeur = 800
hauteur = 600
ecran = pygame.display.set_mode((largeur, hauteur))

# Définir les couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Définir la police d'écriture
police = pygame.font.Font(None, 36)

# Définir le texte du bouton "JOUER"
texte_jouer = police.render("JOUER", True, noir)

# Obtenir les dimensions du texte du bouton "JOUER"
texte_jouer_rect = texte_jouer.get_rect()

# Positionner le bouton "JOUER" au centre de l'écran
texte_jouer_rect.center = (largeur // 2, hauteur // 2)

# Définir les niveaux
niveaux = []
for page in range(5):
    niveaux_page = []
    for lvl in range(5):
        niveaux_page.append(f"Page {page + 1}, Niveau {lvl + 1}")
    niveaux.append(niveaux_page)

# Variables pour suivre les pages et niveaux actuels
page_actuelle = 0
niveau_actuel = 0

# Boucle principale du jeu
en_cours = True
while en_cours:
    # Gérer les événements
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False
        elif evenement.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si le bouton "JOUER" a été cliqué
            if texte_jouer_rect.collidepoint(evenement.pos):
                # Afficher les niveaux de la page actuelle
                for i, niveau in enumerate(niveaux[page_actuelle]):
                    print(f"Niveau {i + 1}: {niveau}")

    # Effacer l'écran
    ecran.fill(blanc)

    # Afficher le bouton "JOUER"
    ecran.blit(texte_jouer, texte_jouer_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()