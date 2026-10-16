chasove = float(input("Vuvedi otraboteni chasove: "))
zaplashtane = float(input("Vuvedi zaplashtane na chas: "))
bonus = float(input("Vuvedi bonus v procenti: "))
udrazhka = float(input("Vuvedi udrazhka v procenti: "))

zaplata = chasove * zaplashtane
zaplata = zaplata * (1 + bonus / 100)
zaplata = zaplata * (1 - udrazhka / 100)

print(f"Kraino vuznagrazhdenie: {zaplata:.2f}")