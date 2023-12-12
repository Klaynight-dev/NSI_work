absorb=12
absorb_sav=absorb
compteur=0
while absorb >= 1:
    absorb=absorb/2
    compteur=compteur+1

print ("Pour absorber", absorb_sav,"mg il faut",compteur*25,"min pour éliminé toute l'iode")    
