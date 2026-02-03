'''
Lielākais no trīs skaitļiem
Ievade: trīs veseli skaitļi
Uzdevums: izvada lielāko skaitli. Papildus: paziņo, ja visi 3 vienādi

'''
sk1 = int(input('Ievadi sk1='))
sk2 = int(input('Ievadi sk2='))
sk3 = int(input('Ievadi sk3='))
if sk1 == sk2 == sk3:
    print('Visi skaitļi vienādi')
elif sk1 >= sk2 and sk1 >= sk3:
    print('Lielākais skaitlis',sk1)
elif sk2 >= sk1 and sk2 >= sk3:
    print('Lielākais skaitlis',sk2)
else:
    print('Lielākais skaitlis',sk3)