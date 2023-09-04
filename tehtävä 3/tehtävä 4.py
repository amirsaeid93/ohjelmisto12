
vuosi = int(input("Syötä vuosi-numero:"))

if vuosi > 100 and vuosi % 4 == 0 and vuosi % 400 == 0:
    print(vuosi, "on karkausvuosi.")
elif vuosi < 100 and vuosi % 4 == 0:
    print(vuosi, "on karkausvuosi.")
else:
    print(vuosi, "ei ole karkausvuosi.")

