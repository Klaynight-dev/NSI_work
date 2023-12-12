import pygame 
def jeu():
    pygame.init()
    ecran = pygame.display.set_mode((600, 600))
    image = pygame.image.load("R.png").convert_alpha()
    image2 = pygame.image.load("hero.png").convert_alpha()
    image3 = pygame.image.load("enemi.png").convert_alpha()
    Blanc=(255, 255, 255)
    Red=(255,75,0)
    continuer = True
    arial_font=pygame.font.SysFont("arial", 30)
    text=arial_font.render(f"points de vie : 10",True, Red)
    ecran.blit(text, (200, 430))
    while continuer:
        pygame.draw.rect(ecran, Blanc, pygame.Rect(150, 100, 300, 300))
        decalY=70
        for i in range(10):
            decal=150
            decalY=decalY+30
            for x in carte[0+i]:
                if x==1:
                    ecran.blit(image, (decal, decalY))
                    decal=decal +30
                if x==0:
                    decal=decal+30
                if x==2:
                    ecran.blit(image2, (decal, decalY))
                    decal=decal+30
                if x==3:
                    ecran.blit(image3, (decal, decalY))
                    decal=decal+30
                
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
        pygame.display.flip()
    pygame.quit()
carte=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [2, 0, 0, 0, 1, 0, 0, 0, 0, 4],
       [1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
       [1, 3, 0, 0, 1, 3, 1, 0, 1, 1],
       [1, 0, 1, 1, 1, 0, 1, 3, 1, 1],
       [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
       [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
jeu()