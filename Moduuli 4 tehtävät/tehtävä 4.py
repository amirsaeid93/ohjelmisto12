import random

valittu_numero = random.randint(1, 10)

arvaukset = 0

while True:

    try:
        arvaus = int(input("Arvaa valitsemani numero 1 ja 10 väliltä:"))
    except ValueError:
        print("Väärä syöttö. Syötä kelvollinen numero.")
        continue


    arvaukset += 1

    if arvaus < valittu_numero:
        print("Numero on liian pieni, yritä uudelleen.")
    elif arvaus > valittu_numero:
        print("Numero on liian iso, yritä uudelleen.")
    else:
        print(f"Oikein. Arvasit {arvaukset} arvauksella.")
        break
