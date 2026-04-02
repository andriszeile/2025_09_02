import random
tsumma = 0
sdienas = 0
for diena in range(1, 8):
    dtemp = random.randint(-10, 30)
    print(f'{diena}.dienas temperatūra ir {dtemp}')
    tsumma += dtemp
    if dtemp > 20:
        sdienas += 1
vtemp = tsumma / 7
print(f'vidējā temperatūra ir {vtemp:.1f}')
print(f'Silto dienu skaits ir {sdienas}')