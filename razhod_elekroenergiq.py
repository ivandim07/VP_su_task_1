moshtnost = float(input("Vuvedi moshtnost v vatove: "))
chasove = float(input("Vuvedi chasove na den: "))
dni = int(input("Vuvedi broi dni: "))
cena = float(input("Vuvedi cena na kWh: "))

potreblenie = moshtnost / 1000 * chasove * dni
obshta_cena = potreblenie * cena

print(f"Potreblenie: {potreblenie:.2f}")
print(f"Obshta cena: {obshta_cena:.2f}")