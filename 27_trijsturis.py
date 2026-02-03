'''
Trijstūra eksistence
Ievade: trīs malas
Uzdevums: pārbaudi, vai no šīm malām var izveidot trijstūri.
(divu malu summai jābūt lielākai par trešo malu)
and - loģiskais un
or - loģiskais vai
izt1 or izt2 - ja vismaz viena izteiksme patiesa = kopējais patiess
izt1 and izt2 - ja visas izteiksmes patiesas, tikai tad kopējais patiess
'''
m1 = int(input('Ievadi garumu m1='))
m2 = int(input('Ievadi garumu m2='))
m3 = int(input('Ievadi garumu m3='))

if (m1 + m2) > m3 and (m1 + m3) > m2 and (m2 + m3) > m1:
    print('Sanāk trijstūris')
else:
    print('Trijstūris nesanāk')