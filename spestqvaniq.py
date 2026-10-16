nachalna_suma = float(input("Nachalna suma: "))
god_lihven_procent = float(input("Godishen lihven procent: "))
godini = int(input("Godini: "))

natrupana_lihva = nachalna_suma * god_lihven_procent / 100 * godini
obshta_suma = nachalna_suma + natrupana_lihva

print(f"Natrupana lihva: {natrupana_lihva:.2f}")
print(f"Obshta suma: {obshta_suma:.2f}")