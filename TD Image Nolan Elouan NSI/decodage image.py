from PIL import Image
from PIL import Image, ImageEnhance                                         # Importation des librairies Python Imaging Library
im1 = Image.open("mouette+secret.png")                                      # Ouverture de l'image de décodage
                                                                            #
def convert(couleur):                                                       # Définition de la fonction convertion avec comme parramètre la couleur
    temp = "{0:b}".format(couleur)                                          # Séparation des couleur RGB en binaire
    temp.split()                                                            # Permet de séparer l'octet en bit
                                                                            # 
    while len(temp)<8:                                                      # Si il y a des 0 logiques dans l'octect qui n'est pas précédé d'un 1 logique, il ne s'affiche pas, donc cette boucle permet de mettre les 0 logiques dans l'octet. Elle compare si temp soit le mot binaire est bien constitué de 8 carractère si non elle le lui rajoute 1 jusqu'à se que il fasse 8 bits
        temp="0"+temp                                                       # Cette opération rajoute un 0 logique à l'avant du mot binaire
                                                                            # 
    val=temp[4]+temp[5]+temp[6]+temp[7]                                     # prend les bits caché dans les bits de poids faible
    val=val+"0000"                                                          # Rajoute que des 0 logique en bit de poids faibles
                                                                            # 
    a=int(val[0])*2**7+int(val[1])*2**6+int(val[2])*2**5+int(val[3])*2**4   # multiplie les bits par leur valeur binair (ex : le bit de poids faible = 1 et le bit de poids fort = 128)
    return a                                                                # retourne notre valeur
                                                                            # 
largeur,hauteur=im1.size                                                    # Définie la largeur et la hauteur de l'image (cela permet au programe d'être modulable si on a une image en 4k ou en 480p)
                                                                            # 
for x in range(0,largeur,1):                                                # Boucle sur l'axe horizontal
    for y in range(0,hauteur,1):                                            # Boucle sur l'axe vertical
        rouge,vert,bleu = im1.getpixel((x,y))                      # Assigne au variable rouge vert et bleu leur couleur en rgb respectif, la variable inutile ne sert juste qu'à évité une erreur de non assignation de variable
        im1.putpixel((x,y),(convert(rouge),convert(vert),convert(bleu)))    # convertie tout le RGB des pixel via la fonction convert, qui permet de mettre les bits de poids faible en bits de poids forts
                                                                            # 
im1.show()                                                                  # nous montre le rendu de l'image
im1.save("secret-mouette.png")                                              # Sauvegarde l'image avec son nom