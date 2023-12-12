import hashlib
from datetime import datetime

def attaque_brute_force_hash(h):
    nbr=0
    n=0
    t0 = datetime.now() # l'heure à l'instant présent
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for length in range(1, 9):
        if length >= 1:
            for a in alphabet:
                mot = a
                n+=1
                if hashlib.sha256(mot.encode()).hexdigest() == h:
                    print()
                    print("TROUVÉ ! '{}' a le hash {},".format(mot, h))
                    print("{} mot(s) ont été testés en {} seconde(s).".format(n, (datetime.now() - t0).total_seconds()))
                    return
                if length >= 2:
                    for b in alphabet:
                        mot = a + b
                        n+=1
                        if hashlib.sha256(mot.encode()).hexdigest() == h:
                            print()
                            print("TROUVÉ ! '{}' a le hash {},".format(mot, h))
                            print("{} mot(s) ont été testés en {} seconde(s).".format(n, (datetime.now() - t0).total_seconds()))
                            return
                        if length >= 3:
                            for c in alphabet:
                                mot = a + b + c
                                n+=1
                                if hashlib.sha256(mot.encode()).hexdigest() == h:
                                    print()
                                    print("TROUVÉ ! '{}' a le hash {},".format(mot, h))
                                    print("{} mot(s) ont été testés en {} seconde(s).".format(n, (datetime.now() - t0).total_seconds()))
                                    return
                                if length >= 4:
                                    for d in alphabet:
                                        mot = a + b + c + d
                                        n+=1
                                        if hashlib.sha256(mot.encode()).hexdigest() == h:
                                            print()
                                            print("TROUVÉ ! '{}' a le hash {},".format(mot, h))
                                            print("{} mot(s) ont été testés en {} seconde(s).".format(n, (datetime.now() - t0).total_seconds()))
                                            return
                                        if length >= 5:
                                            for e in alphabet:
                                                mot = a + b + c + d + e
                                                n+=1
                                                if hashlib.sha256(mot.encode()).hexdigest() == h:
                                                    print()
                                                    print("TROUVÉ ! '{}' a le hash {},".format(mot, h))
                                                    print("{} mot(s) ont été testés en {} seconde(s).".format(n, (datetime.now() - t0).total_seconds()))
                                                    return
                                                if n % 100000 == 0:
                                                            nbr+=0.1
                                                            print(f"{'%.1f' % nbr}M de mot testé.", end="\r")
                                                if length >= 6:
                                                    for f in alphabet:
                                                        mot = a + b + c + d + e + f
                                                        n+=1
                                                        if hashlib.sha256(mot.encode()).hexdigest() == h:
                                                            print()
                                                            print("TROUVÉ ! '{}' a le hash {},".format(mot, h))
                                                            print("{} mot(s) ont été testés en {} seconde(s).".format(n, (datetime.now() - t0).total_seconds()))
                                                            return
                                                        if n % 100000 == 0:
                                                            nbr+=0.1
                                                            print(f"{'%.1f' % nbr}M de mot(s) testé(s).", end="\r")
                                                        if length >= 7:
                                                            for g in alphabet:
                                                                mot = a + b + c + d + e + f + g
                                                                n+=1
                                                                if hashlib.sha256(mot.encode()).hexdigest() == h:
                                                                    print()
                                                                    print("TROUVÉ ! '{}' a le hash {},".format(mot, h))
                                                                    print("{} mot(s) ont été testés en {} seconde(s).".format(n, (datetime.now() - t0).total_seconds()))
                                                                    return
                                                                if n % 100000 == 0:
                                                                    nbr+=0.1
                                                                    print(f"{'%.1f' % nbr}M de mot(s) testé(s).", end="\r")
                                                                if length >= 8:
                                                                    for h in alphabet:
                                                                        mot = a + b + c + d + e + f + g + h
                                                                        n+=1
                                                                        if hashlib.sha256(mot.encode()).hexdigest() == h:
                                                                            print()
                                                                            print("TROUVÉ ! '{}' a le hash {},".format(mot, h))
                                                                            print("{} mot(s) ont été testés en {} seconde(s).".format(n, (datetime.now() - t0).total_seconds()))
                                                                            return
                                                                        if n % 100000 == 0:
                                                                            nbr+=0.1
                                                                            print(f"{'%.1f' % nbr}M de mot(s) testé(s).", end="\r")

    print()
    print("{} mot(s) ont été testés en {} seconde(s),".format(n, (datetime.now() - t0).total_seconds()))
    print("Aucun des mots testés n'avait le hash {}.".format(h))

h = input("Veuillez entrer un mot de 1 à 6 lettre(s) en minuscule(s) : ")
h = hashlib.sha256(h.encode()).hexdigest()

attaque_brute_force_hash(h)
