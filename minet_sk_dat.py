minimums = 1
maksimums = 100
print('Iedomājies skaitli intervālā no',minimums,'līdz',maksimums,'ieskaitot.')
meginajumi = 0
while True:
    minejums = (minimums + maksimums) // 2
    print('Vai iedomātais skaitlis ir',minejums)
    meginajumi += 1
    atb = input('(L)ielāks, (M)azaks, (U)zminēji').lower()
    if atb == 'l':
        minimums = minejums
    elif atb == 'm':
        maksimums = minejums
    else:
        print('Uzminēju no',meginajumi,'mēģinājumiem.')
        break