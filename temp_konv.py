"""
Temperatūras pārveidotājs

Ievade: grādi pēc Celsija C
Izvade: Fārenheiti 
formula konvertācijai - F = C * 9/5 + 32
"""
c = float(input('Ievadi Celsija grādu lielumu:'))
f = c * 9 / 5 + 32
print('Konvertējot Fārenheitos ir', f)