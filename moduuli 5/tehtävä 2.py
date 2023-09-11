numbers = []


while True:
    user_input = input("Syötä joku luku tai paina entteriä lopettaaksesi: ")

    if user_input == "":
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Virheellinen syöttö. Syötä joku luku: ")

if len(numbers) >= 5:
    numbers.sort(reverse=True)

    print("Viisi suurinta syöttämääsi lukua suuruus järjestyksessä isoimmasta pienempään ovat: ")
    for num in numbers[:5]:
        print(num)
else:
    print("Ei syötetty tarpeeksi lukuja, jotta voitaisiin määrittää niistä viisi suurinta.")
