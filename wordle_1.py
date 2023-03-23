#VARIANTA NEOPTIMIZATA
#AVERAGE EXECUTION TIME: 2.9642395687500085 minutes

import time
from subprog import citire, extragere, comparatie, selectare, calcul_entropie

timp_start=time.perf_counter()
cuvinte=citire("words.txt")
lista_entr=calcul_entropie(cuvinte)
print(len(cuvinte))
for element in lista_entr:
    print(element)
lista_rezultate=[]
lista_rezultate.append(lista_entr[0])
cuvant_de_ghicit=extragere(cuvinte)
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