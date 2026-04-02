'''
Uzdevums: “Laimes automāts” (slot machine)
Izveido Python programmu, kas simulē vienkāršu spēļu automātu.
📌 Nosacījumi:
Lietotājam sākumā ir 10 monētas.
Katrs grieziens maksā 1 monētu.
Katru reizi programma izlozē 3 nejaušus skaitļus no 1 līdz 5.
Ja:
visi 3 skaitļi vienādi → lietotājs iegūst +5 monētas
2 skaitļi vienādi → +2 monētas
visi dažādi → neko neiegūst
Spēle turpinās ar while, kamēr ir monētas.
Pēc katra gājiena:
izvada izlozētos skaitļus
parāda monētu skaitu
'''
import random
monetas = 10
while monetas > 0:
    print(f'Jums ir pieejamas {monetas} monētas.')
    izvele = input('Vai griezt? (j/n): ').lower()
    if izvele !='j':
        print('Spēle pabeigta.')
        break
    monetas -= 1
    sk = []
    for i in range(3):
        cipars = random.randint(1, 6)
        sk.append(cipars)
    print(f'Rezultāts: {sk[0]} | {sk[1]} | {sk[2]}')
    if sk[0] == sk[1] == sk[2]:
        print('JackPot!!! +5 monētas')
        monetas += 5
    elif sk[0] == sk[1] or sk[1] == sk[2] or sk[0] == sk[2]:
        print('Divi vienādi! +2 monētas')
        monetas += 2
    else:
        print('Nav vinnēts.')
if monetas == 0:
    print('Monētas beidzās. Nav pieejama spēle.')
else:
    print(f'Spēle beidzās. Tev palika {monetas} monētas.')