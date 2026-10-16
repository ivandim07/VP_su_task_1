km_avtobus = float(input("Vuvedi kilometri s avtobus: "))
km_taxi = float(input("Vuvedi kilometri s taxi: "))
cena_avtobus = float(input("Vuvedi cena za kilometur s avtobus: "))
cena_taxi = float(input("Vuvedi cena za kilometur s taxi: "))

razstoyanie = km_avtobus + km_taxi
cena = km_avtobus * cena_avtobus + km_taxi * cena_taxi

print(f"Obshto razstoyanie: {razstoyanie:.2f} km")
print(f"Obshta cena: {cena:.2f} lv.")