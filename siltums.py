par = 0
pret = 0
for maja in range(1, 6):
    for dzivoklis in range(1, 13):
        print(f'Māja nr.{maja} dzīvoklis nr.{dzivoklis}')
        jautajums = input('Vai piekrītat apkures sezonas beigām? (j/n) - ').lower()
        if jautajums == 'j':
            par += 1
        else:
            pret += 1
print(f'Par nobalsoja: {par}')
print(f'Pret nobalsoja: {pret}')
print(f'Par % nobalsoja: {par/60*100:.2f}')
print(f'Pret % nobalsoja: {pret/60*100:.2f}')
if par/60*100 > 50:
    print('Apkures sezona tiks noslēgta.')
else:
    print('Apkures sezona netik noslēgta.')