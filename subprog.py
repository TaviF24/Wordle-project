from math import log2
from random import choice
def citire(numefisier):                                             #citirea fisierului
    with open(numefisier) as f:
        cuvinte=f.read().split()
    return cuvinte

def extragere(lista):                                               #extragerea aleatorie a unui cuvant din lista
    cuvant=choice(lista)
    return cuvant

def comparatie(cuvant1,cuvant2):                                    #compararea a doua cuvinte, obtinand un "sablon", unde simbolul '$' inseamna verde,
    rezultat=["*"]*5                                                #simbolul '|' inseamna galben, iar simbolul '*' inseamna gri
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

def verificare(cuvant1_din_lista_mare,cuvant2_de_ghicit,cuvant_random,sablon):         #verific daca cuvantul din lista de cuvinte (cuvant1_din_lista_mare)
    for semn in range(len(sablon)):                                                    #este o posibilitate pentru cuvantul pe care trebuie sa-l ghicesc
        if sablon[semn]=='$':                                                          #(cuvant2_de_ghicit) folosindu-ma de cuvantul cu entropia cea mai buna
            if cuvant2_de_ghicit[semn]!=cuvant1_din_lista_mare[semn]:                  #la momentul respectiv (cuvant_random) si de sablonul creat la subprogramul
                break                                                                  #'comparatie'
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

def selectare(sablon,lista,cuvant_de_ghicit,cuvant_random):                         #elimin din lista de cuvinte, cuvintele care nu ma ajuta sa ghicesc cuvantul,
    indice=0                                                                        #folosind subprogramul 'verificare'
    while indice<len(lista):
        if verificare(lista[indice],cuvant_de_ghicit,cuvant_random,sablon)==0:
            del lista[indice]
        else:
            indice+=1
    return lista

def calcul_entropie(lista):                                                         #calculez entropia fiecarui cuvant, folosind lista de la momentul respectiv
    dictionar = {}                                                                  #si o sorterz descrescator dupa ecntropie
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