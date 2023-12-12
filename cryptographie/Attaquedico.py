import hashlib
from datetime import datetime 

def attaque_dico_hash(h, dic):
    loader=["/ ","― ",'\ ','| ']
    dico = open(dic, mode="r", encoding="utf-8", errors="ignore")
    n = 0   # pour compter le nombre de mots
    t0 = datetime.now() # l'heure à l'instant présent

    for mot in dico:
      mot = mot.strip()
      n = n + 1

      if hashlib.sha256(mot.encode()).hexdigest() == h:
          print()
          print("TROUVÉ ! Le mot '{}' a le hash {},".format(mot,h))
          print("{} mot(s) ont étés testés en {} seconde(s).".format(n, (datetime.now()-t0).total_seconds()))
          dico.close()
          return

      if n % 100000 == 0:
          nbr=n/1000000
          for i in loader
          print(f"{'%.1f' % nbr}M de mots de passes testés."+load, end="\r")

    print()
    print("{} mot(s) ont étés testés en {} seconde(s),".format(n, (datetime.now()-t0).total_seconds()))
    print("Aucun des mots testés n'avait le hash {}.".format(h))

h="b801016c1e885ddbe909cef8adc967ef15cda64ba084059ed04cc77e491d7fa0"
dic="realhuman_phill.txt"
attaque_dico_hash(h, dic)