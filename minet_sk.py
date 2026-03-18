import random

datora_sk = random.randint(1, 1000)
print('Es iedomājos skaitli apgabalā no 1 līdz 100, uzmini to!')
meginajumi = 0
while True:
    minetais_sk = int(input('Ievadi savu minējumu: '))
    meginajumi += 1
    if minetais_sk > datora_sk:
        print('Neuzminēji. Mans skaitlis ir mazāks!')
    elif minetais_sk < datora_sk:
        print('Neuzminēji. Mans skaitlis ir lielāks!')
    else:
        print('Uzminēji, izmantojot',meginajumi,'mēģinājumus!')
        break
