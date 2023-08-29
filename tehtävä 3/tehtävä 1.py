kuha = float(input("Mikä on kalastamasi kuhan pituus senttimetreinä?"))
if (kuha<37):
    print("Päästä kuha takaisin mereen, koska kalastamasi kuha on ", (37-kuha), " cm liian lyhyt syötäväksi.")
if (kuha>=37):
    print("Kuhasi on tarpeeksi iso syötäväksi.")
