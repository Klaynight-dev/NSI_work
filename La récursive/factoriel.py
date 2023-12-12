def factoriel(n):
    assert n>=0, f"Veuillez entrer un nombre positif !"
    if n==1:
        return n
    else:
        return n*factoriel(n-1)

print(factoriel(4))
