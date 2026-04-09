import random
meginajumi = 0
trapijumi = 0
while True:
    ievade = input('Ievadi skaitli 1..5 vai stop lai beigtu spēlēt: ')
    if ievade == 'stop':
        break
    merkis = random.randint(1, 5)
    meginajumi += 1
    if merkis == int(ievade):
        print('Trāpīts')
        trapijumi += 1
    else:
        print(f'Garām, bija {merkis}.')
print(f'Spēle beigusies, veikti {meginajumi} mēģinājumi.')
precizitate = trapijumi/meginajumi*100
print(f'Tava precizitāte ir {precizitate:.2f}%.')
if precizitate > 50:
    print('Tu esli labs šāvējs.')