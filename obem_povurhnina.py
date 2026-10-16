dulzhina = float(input("Vuvedi dulzhina: "))
shirina = float(input("Vuvedi shirina: "))
visochina = float(input("Vuvedi visochina: "))

obem = dulzhina * shirina * visochina
povurhnina = 2 * (dulzhina * shirina + dulzhina * visochina + shirina * visochina)

print(f"Obem: {obem:.3f}")
print(f"Povurhnina: {povurhnina:.3f}")