while True:
    tuuma = float(input("Minkä tuumainen?"))

    if tuuma < 0:
        print("Ohjelma lopetettu.")
        break

    cm = tuuma * 2.54

    print(f"{tuuma} tuumaa on {cm} senttimetriä.")
