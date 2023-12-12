def anniv (naissances,mois):
    
    fortinayt=[]
    
    for i in naissances:
        
        if naissances[i] == mois:
            fortinayt.append(i)
    return fortinayt


naissances = {'Amosus': 10, 'Gigachad': 12, 'FilthyFrank': 7, 'Mahmoud' : 12, 'nikzbi' : 6}

lakaka=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Decembre"]


mois=int(input("quel est votre mois: "))
mamacita=anniv(naissances, mois)
print(mamacita,"est/sont né(s) le",mois ,"eme mois")