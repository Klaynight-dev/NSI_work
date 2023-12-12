def somme(n):
    if n==0:
        return n
    else:
        return n+somme(n-1)

print(somme(982))