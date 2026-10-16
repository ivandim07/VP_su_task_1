hrana = float(input("Vuvedi stoinost na hranata: "))
napitki = float(input("Vuvedi stoinost na napitkite: "))
taksa = float(input("Vuvedi taksa v procenti: "))
hora = int(input("Vuvedi broi hora: "))

smetka = (hrana + napitki) * (1 + taksa / 100)
na_chovek = smetka / hora

print(f"Obshta smetka: {smetka:.2f}")
print(f"Suma na chovek: {na_chovek:.2f}")