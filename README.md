from PIL import Image                                                                                                                           
from PIL import Image, ImageEnhance                                                                                                             # Importation des librairies Python Imaging Library
im1 = Image.open("mouette.jpg")                                                                                                                 # Ouverture de l'image de codage
im2 = Image.open("secret.jpg")                                                                                                                  # Ouverture de l'image à encoder
                                                                                                                                                # 
def convert(couleur, couleur2):                                                                                                                 # Définition de la fonction convertion avec comme parramètre la couleur
    temp = "{0:b}".format(couleur)                                                                                                              # Séparation des couleur RGB en binaire
    temp.split()                                                                                                                                # Permet de séparer l'octet en bit
                                                                                                                                                # 
    while len(temp)<8:                                                                                                                          # Si il y a des 0 logiques dans l'octect qui n'est pas précédé d'un 1 logique, il ne s'affiche pas, donc cette boucle permet de mettre les 0 logiques dans l'octet. Elle compare si temp soit le mot binaire est bien constitué de 8 carractère si non elle le lui rajoute 1 jusqu'à se que il fasse 8 bits
        temp="0"+temp                                                                                                                           # Cette opération rajoute un 0 logique à l'avant du mot binaire
                                                                                                                                                # 
    temp2 = "{0:b}".format(couleur2)                                                                                                            # 
    temp2.split()                                                                                                                               #
                                                                                                                                                # 
    while len(temp2)<8:                                                                                                                         # 
        temp2="0"+temp2                                                                                                                         # 
                                                                                                                                                # 
    val=temp[0]+temp[1]+temp[2]+temp[3]                                                                                                         # 
    val2=temp2[0]+temp2[1]+temp2[2]+temp2[3]                                                                                                    # 
    val=val+val2                                                                                                                                # 
                                                                                                                                                # 
    a=int(val[0])*2**7+int(val[1])*2**6+int(val[2])*2**5+int(val[3])*2**4+int(val[4])*2**3+int(val[5])*2**2+int(val[6])*2**1+int(val[7])*2**0   # 
    val=a                                                                                                                                       # 
    return val                                                                                                                                  # 
                                                                                                                                                # 
largeur,hauteur=im1.size                                                                                                                        # 
for x in range(0,largeur,1):                                                                                                                    # 
    for y in range(0,hauteur,1):                                                                                                                # 
        (rouge,vert,bleu) = im1.getpixel((x,y))                                                                                                 # 
        (rouge1,vert1,bleu1) = im2.getpixel((x,y))                                                                                              # 
        im1.putpixel((x,y),(convert(rouge,rouge1),convert(vert,vert1),convert(bleu,bleu1)))                                                     # 
                                                                                                                                                # 
im1.show()                                                                                                                                      # 
im1.save("mouette+secret.png") 
