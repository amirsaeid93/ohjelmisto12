# muunnos suhteet
leiviskät_nauloina = 20
naulat_luoteina= 32
luodit_grammoina = 13.3

# kysymykset
leiviskät = float(input("Anna leiviskät.\n"))
naulat = float(input("Anna naulat. \n"))
luodit = float(input("Anna luodit:\n"))

# koko massa luoteina
luodit_yhteensä = (leiviskät * leiviskät_nauloina * naulat_luoteina) + (naulat * naulat_luoteina) + luodit

# muunnos luodeista kilogrammaan ja grammaan
kilogramma = luodit_yhteensä * luodit_grammoina / 1000
gramma = luodit_yhteensä * luodit_grammoina % 1000

# Massa kilogrammana ja grammana
print("\nMassa nykymittojen mukaan:")
print(f"{int(kilogramma)} kilogrammaa ja {gramma:.2f} grammaa.")
