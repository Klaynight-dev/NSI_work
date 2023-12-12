import turtle
import time
import random

# Configuration de la fenêtre
fenetre = turtle.Screen()
fenetre.title("Snake en Python avec Turtle")
fenetre.bgcolor("black")
fenetre.setup(width=600, height=600)
fenetre.tracer(0)

# Tête du serpent
tete = turtle.Turtle()
tete.speed(0)
tete.shape("square")
tete.color("white")
tete.penup()
tete.goto(0, 0)
tete.direction = "Stop"

# Nourriture du serpent
nourriture = turtle.Turtle()
nourriture.speed(0)
nourriture.shape("circle")
nourriture.color("red")
nourriture.penup()
nourriture.goto(0, 100)

segments = []

# Fonctions de déplacement
def aller_haut():
    if tete.direction != "bas":
        tete.direction = "haut"

def aller_bas():
    if tete.direction != "haut":
        tete.direction = "bas"

def aller_gauche():
    if tete.direction != "droite":
        tete.direction = "gauche"

def aller_droite():
    if tete.direction != "gauche":
        tete.direction = "droite"

# Assignation des touches
fenetre.listen()
fenetre.onkeypress(aller_haut, "Up")
fenetre.onkeypress(aller_bas, "Down")
fenetre.onkeypress(aller_gauche, "Left")
fenetre.onkeypress(aller_droite, "Right")

# Fonction de déplacement du serpent
def deplacer():
    if tete.direction == "haut":
        y = tete.ycor()
        tete.sety(y + 20)

    if tete.direction == "bas":
        y = tete.ycor()
        tete.sety(y - 20)

    if tete.direction == "gauche":
        x = tete.xcor()
        tete.setx(x - 20)

    if tete.direction == "droite":
        x = tete.xcor()
        tete.setx(x + 20)

# Boucle principale du jeu
while True:
    fenetre.update()

    # Vérifier les collisions avec la bordure
    if (
        tete.xcor() > 290 or
        tete.xcor() < -290 or
        tete.ycor() > 290 or
        tete.ycor() < -290
    ):
        time.sleep(1)
        tete.goto(0, 0)
        tete.direction = "Stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

    # Vérifier la collision avec la nourriture
    if tete.distance(nourriture) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        nourriture.goto(x, y)

        nouveau_segment = turtle.Turtle()
        nouveau_segment.speed(0)
        nouveau_segment.shape("square")
        nouveau_segment.color("grey")
        nouveau_segment.penup()
        segments.append(nouveau_segment)

    # Déplacer les segments du corps du serpent
    total_segments = len(segments)
    for index in range(total_segments - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if total_segments > 0:
        x = tete.xcor()
        y = tete.ycor()
        segments[0].goto(x, y)

    deplacer()

    # Vérifier la collision avec le corps du serpent
    for segment in segments:
        if segment.distance(tete) < 20:
            time.sleep(1)
            tete.goto(0, 0)
            tete.direction = "Stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

    time.sleep(0.1)
