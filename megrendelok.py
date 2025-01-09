from Megrendeles import Megrendeles

def beolvasas():
    lista = []
    f = open("megrendelok.txt", "r")
    fejlec = f.readline()
    sorok = f.readlines()
    f.close()
    for i in range(0,len(sorok)):
        adatok = sorok[i].strip().split('$')
        datum, rendeles, email = adatok
        megrendeles = Megrendeles(
            datum.strip(),
            int(rendeles.strip()),
            email.strip()
        )
        lista.append(megrendeles)
    return lista

sorok = beolvasas()

def megrendelesek(sorok):
    szama = 0
    for i in range(0,len(sorok),1):
        szama += i
    print("III/A, B:")
    print(f"A megrendelések száma: {szama}")

def krumplifej(sorok):
    kfej = 0
    for i in range(0,len(sorok),1):
        if sorok[i].email == "krumplifej@citromail.hu":
            kfej += 1
    print("III/C:")
    print(f"A „krumplifej@citromail.hu”  címhez tartozó megrendelések száma: {kfej}")

def utolso(sorok):
    maxindex = 0
    kiaz = ""
    for i in range(0,len(sorok),1):
        if sorok[i].rendeles > maxindex:
            kiaz = sorok[i].email
    print("II/D:")
    print(f"A legutolsó rendeléshez tartozó email cím: {kiaz}")