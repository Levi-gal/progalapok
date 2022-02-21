import random
szamok = [ 2 , 5 , 9 , 7 , 3 , 7 , 1 , 8 , 4 , 9 ]
print('Minimum kiválasztáselve: ')
min1 = 1
for x in szamok:
    if x < min1:
        min1 = x
print('Páros számok összege: ')
print(min(szamok))