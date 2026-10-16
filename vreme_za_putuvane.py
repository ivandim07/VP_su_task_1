razstoyanie = float(input("Vuvedi razstoyanie: "))
skorost = float(input("Vuvedi skorost: "))
pochivka = float(input("Vuvedi pochivka v minuti: "))

vreme = razstoyanie / skorost * 60 + pochivka

print(f"Obshto vreme: {vreme:.2f}")