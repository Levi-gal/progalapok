import random
szamok = [ 2 , 5 , 9 , 7 , 3 , 7 , 1 , 8 , 4 , 9 ]
print('Maximum kiválasztáselve: ')
max1 = 1
for x in szamok:
    if x > max1:
        max1 = x
print('Páros számok összege: ')
print(max(szamok))