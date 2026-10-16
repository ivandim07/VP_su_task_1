import math

dulzhina = float(input("Vuvedi dulzhina na poda: "))
shirina = float(input("Vuvedi shirina na poda: "))
plosht_plochka = float(input("Vuvedi plosht na edna plochka: "))
rezerv = float(input("Vuvedi rezerv v procenti: "))
cena = float(input("Vuvedi cena na plochka: "))

plosht_pod = dulzhina * shirina
broi = math.ceil(plosht_pod * (1 + rezerv / 100) / plosht_plochka)
obshta_cena = broi * cena

print(f"Broi: {broi}")
print(f"{obshta_cena:.2f}")