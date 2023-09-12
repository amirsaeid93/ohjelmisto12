def tervehdi(kerrat):
    for i in range(kerrat):
        print ("Hyvää päivää " + str(i+1) + ". kerran")
    return

print ("Päivä alkaa tervehdyksillä.")
# annetaan argumenttina arvo 5
tervehdi(1)
print ("Tervehditään lisää.")
tervehdi(1)
kerrat = int(input("kuinka monta kertaa tervehditään?"))
tervehdi(kerrat)