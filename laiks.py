"""
Laika pārveidošana sekundēs

Ievade: stundas, minūtes, sekundes
Izvade: cik kopā sekundes.
"""
h = int(input("Ievadi stundas: "))
m = int(input("Ievadi minūtes: "))
s = int(input("Ievadi sekundes: "))
sek = h * 3600 + m *60 + s
print("Kopā sekundes", sek)