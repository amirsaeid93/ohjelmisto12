"""Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä
1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
"""
import random

def heitä_noppa():
    return random.randint(1, 6)

def pää_funktio():
    while True:
        result = heitä_noppa()
        print(result)
        if result == 6:
            break

if __name__ == "__main__":
    pää_funktio()
