'''
Trijstūra eksistence
Ievade: trīs malas
Uzdevums: pārbaudi, vai no šīm malām var izveidot trijstūri.
(divu malu summai jābūt lielākai par trešo malu)
'''
m1 = int(input('Ievadi garumu m1='))
m2 = int(input('Ievadi garumu m2='))
m3 = int(input('Ievadi garumu m3='))

if (m1 + m2) > m3:
    print('Sanāk trijstūris')
elif (m1 + m3) > m2:
    print('Sanāk trijstūris')
elif (m2 + m3) > m1:
    print('Sanāk trijstūris')
else:
    print('Trijstūris nesanāk')