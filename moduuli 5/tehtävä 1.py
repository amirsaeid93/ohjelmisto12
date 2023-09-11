import random
def heitä_noppa():
    return random.randint(1, 6)

heitto_kerrat = int(input("Kuinka monta noppa haluat heittää?"))

kokonais_määrä = 0

for _ in range(heitto_kerrat):
    heitto_tulos = heitä_noppa()
    print(f"Roll: {heitto_tulos}")
    kokonais_määrä += heitto_tulos


print(f"Kaikkien {heitto_kerrat} heitettyjen noppien tulosten summa on: {kokonais_määrä}.")
