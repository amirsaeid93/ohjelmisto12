import random

valittu_numero = random.randint(1, 10)

arvaus = 0

while arvaus != valittu_numero:
    arvaus = int(input("Arvaa valitsemani numero 1 ja 10 väliltä:"))
    if arvaus < valittu_numero:
        print("Numero on liian pieni, yritä uudelleen.")

    elif arvaus > valittu_numero:
        print("Numero on liian iso, yritä uudelleen.")
print("Arvasit oikein.")
