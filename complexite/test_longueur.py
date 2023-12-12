import time
import matplotlib.pyplot as plt

def complexe(n):
    """Teste le temps d'execution en fonctio du nombre de tour de boucle"""
    a=0
    temps_start=time.time()
    for i in range(n):
        for y in range(n):
            a+=1
    temps_end=time.time()
    
    return temps_end-temps_start

def graph(stop, y=[], val_test=[]):
    for test in range(1,stop):
        y.append(complexe(test))
        val_test.append(test)
    # Tracer le graphique avec un titre et des étiquettes
    plt.plot(val_test, y)
    plt.title("Graphique de complexité d'un programe à 2 boucles")
    plt.ylabel("Temps(secondes)")
    plt.xlabel("Nombres de répétition par boucle")
    
    # Afficher le graphique
    plt.show()

def main():
    graph(500)

if __name__=="__main__":
    main()