def regisztracio():
    nev = str(input("Név: "))
    email = str(input("Email cím: "))
    jelszo = str(input("Jelszó: "))
    print("I/C:")
    if len(jelszo) > 6:
        print(f"Sikeres regisztráció {nev} ({email})!")
    elif len(jelszo) == 0:
        print("Sikertelen regisztráció (üres jelszó)")
    else:
        print("Sikertelen regisztráció (kevés karakter)")