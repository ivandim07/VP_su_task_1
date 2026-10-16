litri1 = float(input("Vuvedi litri ot purviya sok: "))
cena1 = float(input("Vuvedi cena na purviya sok: "))
litri2 = float(input("Vuvedi litri ot vtoriya sok: "))
cena2 = float(input("Vuvedi cena na vtoriya sok: "))

obshto_litri = litri1 + litri2
obshta_stoinost = litri1 * cena1 + litri2 * cena2
sredna_cena = obshta_stoinost / obshto_litri

print(f"Obshto kolichestvo: {obshto_litri:.2f}")
print(f"Sredna cena: {sredna_cena:.2f}")