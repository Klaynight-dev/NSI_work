liste=['Doherty','Alice',10,'05',2001,'Moustache','Bleu','Bordeaux',33,10052001,'01']

valliste=[]
file = open("nouveau.txt", "w", encoding = 'utf-8')

for i in liste:
    for y in liste:
        if i!=y:
            if type(i)!=int:
                if type(i)!=int or type(y)!=int:
                    print(f"{i}{y}")
                    val=f"{i}{y}"
                    file.write(f"{val}\n")
file.close()
