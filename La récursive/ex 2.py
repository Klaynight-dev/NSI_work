def fonction(n):
    if n==0:
        return 1
    else:
        return 2*fonction(n-1)

def ordre(nbr):
    for i in range(nbr+1):
        print(f"Pour {i} : {fonction(i)}")

ordre(981)