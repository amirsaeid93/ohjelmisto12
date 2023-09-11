def on_alkuluku(luku):
    if luku <= 1:
        return False

    for jaollinen in range(2, int(luku ** 0.5) + 1):
        if luku % jaollinen == 0:
            return False

    return True


luku_käyttäjä = input("Syötä joku kokonaisluku: ")

try:
    luku = int(luku_käyttäjä)
    if on_alkuluku(luku):
        print(f"{luku} on alkuluku.")
    else:
        print(f"{luku} ei ole alkuluku.")
except ValueError:
    print("Väärä syöttö. Syötä jokin kokonaisluku: ")
