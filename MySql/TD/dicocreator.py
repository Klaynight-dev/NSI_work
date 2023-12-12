import random
import string

# Fonction pour générer un prénom aléatoire
def generate_random_firstname():
    length = random.randint(3, 10)  # Longueur du prénom entre 3 et 10 caractères
    firstname = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return firstname

# Générer une liste de milliers de prénoms aléatoires
thousands_of_firstnames = [generate_random_firstname() for _ in range(1000)]

# Afficher les 10 premiers prénoms à titre d'exemple
for i in range(10):
    print(thousands_of_firstnames[i])