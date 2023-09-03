hytti = str(input("Mikä seuraavista hyttiluokista LUX, A, B tai C on hyttisi luokka?"))

if hytti == "LUX":
    print("Hyttisi on parvekkeellinen ja se on yläkannella.")

elif hytti == "A":
    print("Hyttisi on ikkunallinen ja se on autokannen yläpuolella.")

elif hytti == "B":
    print("Hyttisi on ikkunaton, mutta se on autokannen yläpuolella.")

elif hytti == "C":
    print("Hyttisi on ikkunaton ja se on autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka.")
