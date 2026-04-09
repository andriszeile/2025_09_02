import random
tsumma = 0
sdienas = 0
siltaka = -100
vesaka = 100
for diena in range(1, 8):
    dtemp = random.randint(-10, 30)
    if dtemp > siltaka:
        siltaka = dtemp
    if dtemp < vesaka:
        vesaka = dtemp
    if dtemp < 0:
        print(f'{diena}.dienas temperatūra ir {dtemp} - (sals).')
    else:
        print(f'{diena}.dienas temperatūra ir {dtemp}')
    tsumma += dtemp
    if dtemp > 20:
        sdienas += 1
vtemp = tsumma / 7
print(f'vidējā temperatūra ir {vtemp:.1f}')
print(f'Silto dienu skaits ir {sdienas}')
print(f'Vissiltākās dienas temperatūra bija {siltaka} grādi.')
print(f'Visvēsākās dienas temperatūra bija {vesaka} grādi.')