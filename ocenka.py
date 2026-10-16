ocenka1 = int(input("Ocenka1: "))
ocenka2 = int(input("Ocenka2: "))
ocenka3 = int(input("Ocenka3: "))

tejest1 = int(input("Tejest1: "))
tejest2 = int(input("Tejest2: "))
tejest3 = int(input("Tejest3: "))

rezultat = (ocenka1 * tejest1 + ocenka2 * tejest2 + ocenka3 * tejest3) / 100

print(f"Rezultat: {rezultat:.2f}")