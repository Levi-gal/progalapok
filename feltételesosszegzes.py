import random
szamok = [ 2 , 5 , 9 , 7 , 3 , 7 , 1 , 8 , 4 , 9 ]
print('Feltételes összegzés:')
osszeg = 0
for x in szamok:
    if x %2==0:
        osszeg = osszeg +x
print('Páros számok összege: ')
print(osszeg)