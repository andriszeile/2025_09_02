'''
Pieslēgšanās sistēmai
Lietotājs drīkst pieslēgties, ja:
-lietotājvārds ir "admin" vai "skolotajs"
-parole ir "1234"
👉 Uzdevums:
Izveido programmu, kas prasa:
Ievadīt: 
-lietotājvārdu
-paroli
Pārbauda datus un izvada:
"Pieslēgšanās veiksmīga" vai "Nepareizi dati"'''
lietotajv = input('Ievadi lietotājvārdu: ')
parole = input('Ievadi paroli: ')
if (lietotajv == 'admin' or lietotajv == 'skolotajs') and parole == '1234':
    print('Pieslēgšanās veiksmīga!')
else:
    print('Nepareizi dati.')