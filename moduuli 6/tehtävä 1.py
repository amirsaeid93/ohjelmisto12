"""Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä
1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
"""
import random
def heittää():
    noppa = random.randint(1, 6)
    while noppa != 6:
        print(noppa)
        noppa = random.randint(1, 6)
    print("sait 6")
    return


heittää()



