dulzhina = float(input("Vuvedi dulzhina: "))
shirina = float(input("Vuvedi shirina: "))
visochina = float(input("Vuvedi visochina: "))
otvori = float(input("Vuvedi plosht na vratite i prozorcite: "))
pokrivnost = float(input("Vuvedi pokrivnost na boya: "))
cena = float(input("Vuvedi cena na litur: "))

plosht = 2 * (dulzhina + shirina) * visochina - otvori
litri = plosht / pokrivnost
obshta_cena = litri * cena

print(f"Neobhodimi litri: {litri:.2f}")
print(f"Obshta cena: {obshta_cena:.2f}")