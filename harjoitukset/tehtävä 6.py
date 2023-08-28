# muunnos suhteet
leiviskät_nauloina = 20
naulat_luoteina= 32
luodit_grammoina = 13.3

# Get user input for talents, pounds, and lots
leiviskät = float(input("Anna leiviskät.\n"))
naulat = float(input("Anna naulat. \n"))
luodit = float(input("Anna luodit:\n"))

# Calculate the total weight in lots
luodit_yhteensä = (leiviskät * leiviskät_nauloina * naulat_luoteina) + (naulat * naulat_luoteina) + luodit

# Convert lots to kilograms and grams
kilograms = luodit_yhteensä * luodit_grammoina / 1000
grams = luodit_yhteensä * luodit_grammoina % 1000

# Display the converted weight in modern units
print("\nMassa nykymittojen mukaan:")
print(f"{int(kilograms)} kilogrammaa ja {grams:.2f} grammaa.")
