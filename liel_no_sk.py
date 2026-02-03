'''
Lielākais no diviem skaitļiem
Ievade: divi skaitļi
Uzdevums: izvada lielāko skaitli vai paziņo, ka tie ir vienādi.

'''
sk1 = int(input('Ievadi sk1='))
sk2 = int(input('Ievadi sk2='))
if sk1 > sk2:
    print('Lielākais skaitlis ir', sk1)
elif sk1 == sk2:
    print('Skaitļi vienādi')
else:
    print('Lielākais skaitlis ir', sk2)