def codeB(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return codeB(n//2) + str(n%2)

def ordre(nbr):
    liste=[]
    for i in range(nbr+1):
        liste.append(codeB(i))
    return liste

nbr = int(input("Veuillez donner un nombre : "))

representation= codeB(nbr)
print(f"Le codage binaire de {nbr} est : {representation}")

# print(ordre(nbr))