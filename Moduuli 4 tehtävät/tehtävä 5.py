oikea_käyttäjätunnus = "python"
oikea_salasana = "rules"

yritykset = 0

while yritykset < 5:
    käyttäjätunnus = input("Syötä käyttäjätunnus: ")
    salasana = input("Syötä salasana: ")

    if käyttäjätunnus == oikea_käyttäjätunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")
        yritykset += 1

if yritykset == 5:
    print("Pääsy evätty.")
