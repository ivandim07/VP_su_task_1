razstoyanie1 = float(input("Vuvedi razstoyanie na purviya uchastuk: "))
skorost1 = float(input("Vuvedi skorost na purviya uchastuk: "))
razstoyanie2 = float(input("Vuvedi razstoyanie na vtoriya uchastuk: "))
skorost2 = float(input("Vuvedi skorost na vtoriya uchastuk: "))

vreme1 = razstoyanie1 / skorost1
vreme2 = razstoyanie2 / skorost2

obshto_vreme = vreme1 + vreme2
obshto_razstoyanie = razstoyanie1 + razstoyanie2
sredna_skorost = obshto_razstoyanie / obshto_vreme

print(f"Obshto vreme: {obshto_vreme:.2f}")
print(f"Sredna skorost: {sredna_skorost:.2f}")