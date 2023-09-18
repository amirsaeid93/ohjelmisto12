"""Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan"""

import random


def heitä_noppa(sivujen_määrä):
    return random.randint(1, sivujen_määrä)


def pää_funktio():
    sivujen_määrä = int(input("Syötä nopan sivujen lukumöärä: "))

    while True:
        result = heitä_noppa(sivujen_määrä)
        print(result)
        if result == sivujen_määrä:
            break


if __name__ == "__main__":
    pää_funktio()

