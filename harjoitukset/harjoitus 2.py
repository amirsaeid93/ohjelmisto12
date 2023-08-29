# lääke-esimerkki maeterialista 1
ikä = int(input("Anna ikä: "))
if 15<=ikä<18:
    paino = float(input("Anna paino (kg): "))
    if (ikä>=18 or ikä>=15 and paino>=55):
        print("Lääkkeen käyttö on sallittua sinulle.")

if (ikä < 15 or 15 <= ikä < 18 and paino < 55):
    print("lääkkeen käyttö ei ole sallittua sinulle.")












# lääke-esimerkki maeterialista 1
ikä = int(input("Anna ikä: "))
if 15<=ikä<18:
    paino = float(input("Anna paino (kg): "))
if (ikä>=18 or ikä>=15 and paino>=55):
    print("Lääkkeen käyttö on sallittua sinulle.")

if (ikä < 15 or 15 <= ikä < 18 and paino < 55):
    print("lääkkeen käyttö ei ole sallittua sinulle.")