def occurence(tab, n):
    """Prend un nombre et un tableau et revoie sont occurence"""
    occurences=0
    if tab:
        if tab[0]==n:
            occurences+=1
        return occurences+occurence(tab[1:],n)
    return occurences
    
# tab=[4,5,8,7,7,6,3,2,1,5,9,4,0,3,2,4,5,1,0,3,6,8,9,7,4,4,1]
tab=[4,5,8,7,5]
print(occurence(tab,8))