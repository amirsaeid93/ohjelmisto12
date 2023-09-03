
numbers = []


while True:
    user_input = input("Syötä joku numero tai paina entteriä lopettaaksesi.")


    if user_input == "":
        break

    try:

        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Syöttö ei ollut numero, syötä numero")


if len(numbers) > 0:

    smallest = min(numbers)
    largest = max(numbers)


    print(f"Pienin syötetty luku oli: {smallest}")
    print(f"Suurin syötetty luku oli: {largest}")
else:
    print("Numeroa ei syötetty.")
