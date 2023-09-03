import random


pisteiden_määrä = int(input("Syötä pisteiden määrä numerona: "))
pisteet_ympyrän_sisällä = 0


for _ in range(pisteiden_määrä):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)


    if x**2 + y**2 < 1:
        pisteet_ympyrän_sisällä += 1


pi_likiarvo = 4 * pisteet_ympyrän_sisällä / pisteiden_määrä


print(f"Pii:n likiarvo on  {pi_likiarvo}")
