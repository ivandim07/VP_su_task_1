sekundi = int(input("Vuvedi broi sekundi: "))

chasove = sekundi // 3600
minuti = (sekundi % 3600) // 60
ostavashti_sekundi = sekundi % 60

print(chasove)
print(minuti)
print(ostavashti_sekundi)