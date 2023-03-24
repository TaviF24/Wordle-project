#VARIANTA OPTIMIZATA
#AVERAGE EXECUTION TIME: 47.39804516699951 seconds = 0.7899674194499918 minutes

from subprog import citire, extragere, comparatie, selectare,calcul_entropie
import processes
import time
if __name__=='__main__':                                               #__name__ arata modulul in care suntem la momentul actual, il folosim pentru a evita crearea recursiva de subprocese
    timp_start=time.perf_counter()                                     #pornirea cronometrului
    cuvinte=citire("words.txt")                                      #citirea fisierului cu cuvinte
    lista_entr=processes.multiproc()                                     #obtinerea listei de cuvinte sortata descrescator in functie de entropii, folosind multiprocessing
    print(len(cuvinte))
    for element in lista_entr:
        print(element)
    lista_rezultate=[]                                                 #lista in care voi pune incercarile pe care le-am facut
    lista_rezultate.append(lista_entr[0])                              #punerea in lista a celui mai bun cuvant
    cuvant_de_ghicit=extragere(cuvinte)                             #extragerea unui cuvant de ghicit din lista de cuvinte
    print()
    print(f"de ghicit: {cuvant_de_ghicit}")
    print()
    sablon=comparatie(cuvant_de_ghicit,lista_entr[0][0])
    ok=0
    while sablon.count('$')!=len(sablon):
        cuvinte=selectare(sablon,cuvinte,cuvant_de_ghicit,lista_entr[0][0])
        lista_entr=calcul_entropie(cuvinte)
        if len(lista_entr)>0:
            print(f"incercare: {lista_entr[0]}")
            lista_rezultate.append(lista_entr[0])
            sablon = comparatie(cuvant_de_ghicit, lista_entr[0][0])
        else:
            print("nereusit")
            ok=-1
            break
        ok+=1
    print(f"\nDE GHICIT: {cuvant_de_ghicit}\n")
    if ok==-1:
        print(f"Cuvantul {cuvant_de_ghicit} nu a fost gasit")
    else:
        print("Cuvintele incercate au fost:")
        for element in lista_rezultate:
            print(f"{element[0]}, cu entropia: {element[1]}")

    timp_final=time.perf_counter()
    print()
    print(f"execution time: {timp_final-timp_start} seconds = {(timp_final-timp_start)/60} minutes")