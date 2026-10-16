cena = float(input("Vuvedi cena: "))
otstapka1 = float(input("Vuvedi purva otstupka: "))
otstapka2 = float(input("Vuvedi vtora otstupka: "))

cena = cena * (1 - otstapka1 / 100)
cena = cena * (1 - otstapka2 / 100)

print(f"Krainata cena e: {cena:.2f}")