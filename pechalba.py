broi = int(input("Vuvedi broi produkti: "))
prodazhna_cena = float(input("Vuvedi prodazhna cena: "))
dostavna_cena = float(input("Vuvedi dostavna cena: "))
dopulnitelni_razhodi = float(input("Vuvedi dopulnitelni razhodi: "))

prihod = broi * prodazhna_cena
razhod = broi * dostavna_cena + dopulnitelni_razhodi
pechalba = prihod - razhod

print(f"Obsht prihod: {prihod:.2f}")
print(f"Obsht razhod: {razhod:.2f}")
print(f"Pechalba ili zaguba: {pechalba:.2f}")