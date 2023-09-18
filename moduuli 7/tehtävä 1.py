def anna_kuukausi(kuukausi):
    kuukaudet = ("Talvi", "Kevät", "Kesä", "Syksy")

    if kuukausi in (12, 1, 2):
        return kuukaudet[0]  # Winter
    elif kuukausi in (3, 4, 5):
        return kuukaudet[1]  # Spring
    elif kuukausi in (6, 7, 8):
        return kuukaudet[2]  # Summer
    elif kuukausi in (9, 10, 11):
        return kuukaudet[3]  # Autumn
    else:
        return "Väärä kuukausi"


def pää_funktio():
    kuukausi = int(input("Syötä mikä kuukausi on numerona (1-12): "))

    if 1 <= kuukausi <= 12:
        kuukaudet = anna_kuukausi(kuukausi)
        print(f"Vuoden aika joka on {kuukausi} kuukautena on {kuukaudet}.")
    else:
        print("Väärä syöttö. Ole hyvä ja syötä numero 1 ja 12 väliltä.")


if __name__ == "__main__":
    pää_funktio()
