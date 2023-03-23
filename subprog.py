from math import log2
from random import choice
def citire(numefisier):
    with open(numefisier) as f:
        cuvinte=f.read().split()
    return cuvinte

def extragere(lista):
    cuvant=choice(lista)
    return cuvant

def comparatie(cuvant1,cuvant2):
    rezultat=["*"]*5
    copie1=[x for x in cuvant1]
    copie2=[x for x in cuvant2]
    for litera in range(len(cuvant2)):
        if cuvant2[litera]==cuvant1[litera]:
            rezultat[litera]="$"
            copie1[litera]="$"
            copie2[litera]="$"
    for litera in range(len(copie1)):
        if copie2[litera]!="$" and copie2[litera] in copie1:
            rezultat[litera]="|"
            copie1[copie1.index(copie2[litera])]="|"
    return tuple(rezultat)

def verificare(cuvant1_din_lista_mare,cuvant2_de_ghicit,cuvant_random,sablon):
    for semn in range(len(sablon)):
        if sablon[semn]=='$':
            if cuvant2_de_ghicit[semn]!=cuvant1_din_lista_mare[semn]:
                break
        elif sablon[semn]=='|':
            if cuvant_random[semn] not in cuvant1_din_lista_mare or cuvant_random[semn]==cuvant1_din_lista_mare[semn] or cuvant2_de_ghicit.count(cuvant_random[semn])!=cuvant1_din_lista_mare.count(cuvant_random[semn]):
                break
        else:
            tuplu_pt_galben = tuple([cuvant_random[x] for x in range(len(cuvant_random)) if sablon[x] == '|' or sablon[x]=='$'])
            if (cuvant_random[semn] not in tuplu_pt_galben and cuvant_random[semn] in cuvant1_din_lista_mare) or (cuvant_random[semn] in tuplu_pt_galben and cuvant2_de_ghicit.count(cuvant_random[semn])!=cuvant1_din_lista_mare.count(cuvant_random[semn])) :
                break
    else:
        return 1
    return 0

def selectare(sablon,lista,cuvant_de_ghicit,cuvant_random):
    indice=0
    while indice<len(lista):
        if verificare(lista[indice],cuvant_de_ghicit,cuvant_random,sablon)==0:
            del lista[indice]
        else:
            indice+=1
    return lista

def calcul_entropie(lista):
    dictionar = {}
    lista_entr = []
    for indice1 in range(len(lista)):
        dictionar.clear()
        entropie = 0
        for indice2 in range(len(lista)):
            model = comparatie(lista[indice1], lista[indice2])
            if model in dictionar:
                dictionar[model] += 1
            else:
                dictionar[model] = 1
        for cheie in dictionar:
            probabilitate = round(dictionar[cheie] / len(lista), 7)
            # print(cheie,dictionar[cheie],probabilitate,sep=" _ ")
            entropie += probabilitate * log2(1 / probabilitate)
        lista_entr.append((lista[indice1], entropie))
        print(lista[indice1], entropie, sep="  ")
    lista_entr.sort(key=lambda x:x[1], reverse=True)
    return lista_entr