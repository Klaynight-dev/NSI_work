from multiprocessing import Pool
import matplotlib.pyplot as plt
import time

def square(n):
    return n ** 2

if __name__ == '__main__':
    numbers=[]
    for i in range(10000):
        numbers.append(i)
    print('Prêt')
    timel=[]
    processeur=[1,2,3,4]
    for i in processeur:
        with Pool(processes=i) as pool:
            start_time=time.process_time()
            for i in numbers:
                result = square(i)
            end_time=time.process_time()
            timel.append(end_time)
    print(timel)
    plt.plot(processeur, timel)
    plt.xlabel('Nombre processeur')
    plt.ylabel('Temps d\'exécution (ms)')
    plt.title('Graphique d\'exécution')
    plt.show()
