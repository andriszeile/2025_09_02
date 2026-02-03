'''
Skolas stunda vai pārtraukums
Ievade: stundu numurs (1–8)
Uzdevums:
•	1–4 → “rīta stundas”
•	5–7 → “pēcpusdienas stundas”
•	8 → “pagarinātā diena”
•	citādi → “nepareizs stundu numurs”
'''
st = int(input('Ievadi stundas numuru: '))
if 1 <= st <= 4:
    print('Rīta stundas')
elif 5 <= st <= 7:
    print('Pēcpusdienas stundas')
elif st == 8:
    print('Pagarinātā diena')
else:
    print('Nepareizs stundas nr.')