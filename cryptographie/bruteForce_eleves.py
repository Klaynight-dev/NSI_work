import hashlib
from datetime import datetime 

def attaque_brute_force_hash(h):
    n = 0   # pour compter le nombre de mots
    t0 = datetime.now() # l'heure à l'instant présent
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                for d in alphabet:
                    for e in alphabet:
                        for f in alphabet:
                            mot = a+b+c+d+e+f
                            n = n + 1

                            if hashlib.sha256(mot.encode()).hexdigest() == h:
                                print()
                                print("TROUVÉ ! '{}' a le hash {},".format(mot,h))
                                print("{} mot(s) ont étés testés en {} seconde(s).".format(n, (datetime.now()-t0).total_seconds()))
                                return

                            if n % 1000000 == 0:
                                nbr+=1
                                print(f"{nbr}M", end=", ")

    print()
    print("{} mot(s) ont étés testés en {} seconde(s),".format(n, (datetime.now()-t0).total_seconds()))
    print("Aucun des mots testés n'avait le hash {}.".format(h))

h=input("Veuillez entrer un mot de 6 lettre en minuscule : ")
assertion(h)
h=hashlib.sha256(h.encode()).hexdigest()

attaque_brute_force_hash(h)