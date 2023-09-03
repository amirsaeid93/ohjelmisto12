sukupuoli = str(input("Mikä on sukupuolesi M vai N?"))
hemoglobiini = float(input("Mikä on hemoglobiini arvosi?"))
if sukupuoli == "M" and hemoglobiini < 134:
    print("Hemoglobiiinisi on alhainen.")

elif sukupuoli == "M" and hemoglobiini >= 134 and hemoglobiini <= 195:
    print("Hemoglobiinisi on normaali.")

elif sukupuoli == "M" and hemoglobiini > 195:
    print("Hemoglobiinisi on korkeaa.")

elif sukupuoli == "N" and hemoglobiini < 117:
    print("Hemoglobiinisi on alhainen.")

elif sukupuoli == "N" and hemoglobiini >= 117 and hemoglobiini <= 175:
    print("Hemoglobiinisi on normaali.")

elif sukupuoli == "N" and hemoglobiini > 175:
    print("Hemoglobiinisi on korkeaa.")