import random

def randomszam():
    lista = []
    betus = ""
    for i in range(0,6,1):
        szam = random.randint(0,10)
        lista.append(szam)
    return lista

szamlista = randomszam()

def nagyobb(lista):
    esetekszama = 0
    for i in range(1,len(lista),1):
        if (lista[i] > lista[i-1]):
            esetekszama += 1
    return esetekszama

esetek = nagyobb(szamlista)

def konzol_kiir():
    print("\nII/A, B, C:")
    print(szamlista)    
    print("\nII/D, E:")
    print(f"Nagyobb számok száma: {esetek}.")

def fajlba_ir(esetek):
    f = open("vegeredmeny.txt","a")
    f.write("\nII/F:\n")
    f.write(f"Nagyobb számok száma: {esetek}.")