from multiprocessing import Process, Queue
import multiprocessing
from subprog import citire, comparatie
import math
def calcul_entropie(lista,inc,sf,coada):
    dictionar = {}
    lista_entr = []
    for indice1 in range(inc,sf):
        dictionar.clear()
        entropie = 0
        for indice2 in range(len(lista)):
            model = comparatie(lista[indice1], lista[indice2])
            if model in dictionar:
                dictionar[model] += 1
            else:
                dictionar[model] = 1
        for cheie in dictionar:
            probabilitate = dictionar[cheie] / len(lista)
            entropie += probabilitate * math.log2(1 / probabilitate)
        lista_entr.append((lista[indice1], entropie))
        print(lista[indice1], entropie, sep="  ")
    coada.put(lista_entr)

def multiproc():
    cuvinte = citire("words.txt")
    coada = Queue()
    p1 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 0, 689, coada))
    p2 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 689, 1378, coada))
    p3 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 1378, 2067, coada))
    p4 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 2067, 2756, coada))
    p5 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 2756, 3444, coada))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    rez = []
    while not coada.empty():
        rez.extend(coada.get())
    p1 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 3444, 4133, coada))
    p2 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 4133, 4822, coada))
    p3 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 4822, 5511, coada))
    p4 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 5511, 6200, coada))
    p5 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 6200, 6888, coada))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    while not coada.empty():
        rez.extend(coada.get())
    p1 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 6888, 7577, coada))
    p2 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 7577, 8266, coada))
    p3 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 8266, 8955, coada))
    p4 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 8955, 9644, coada))
    p5 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 9644, 10332, coada))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    while not coada.empty():
        rez.extend(coada.get())
    p1 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 10332, 10519, coada))
    p2 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 10519, 10706, coada))
    p3 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 10706, 10893, coada))
    p4 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 10893, 11080, coada))
    p5 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 11080, 11267, coada))
    p6 = multiprocessing.Process(target=calcul_entropie, args=(cuvinte, 11267, 11454, coada))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    while not coada.empty():
        rez.extend(coada.get())
    rez.sort(key=lambda x: x[1], reverse=True)
    return rez