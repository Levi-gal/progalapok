import random
szamok = [ 2 , 5 , 9 , 7 , 3 , 7 , 1]
db = 0

for x in szamok:
    if x == 3:
        db = db + 1

print('A hármasok száma: ')
print(db)