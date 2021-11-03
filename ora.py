import random
while True:
   input("Nyomj ENTERT a dobáshoz")

   number = random.randint(1,6)
   if number == 1:
    print("Amit kaptál: ",number)
    print('. . .')
    print('. * .')
    print('. . .')
   elif number == 2:
    print('. . .')
    print('* . *')
    print('. . .')
   elif number == 3:
    print('. . *')
    print('. * .')
    print('* . .')
   elif number == 4:
    print('* . *')
    print('. . .')
    print('* . *')
   elif number == 5:
    print('* . *')
    print('. * .')
    print('* . *')
   elif number == 6:
    print('* . *')
    print('* . *')
    print('* . *')


    option = input("Újra dobsz?(Yes/No) ")

    if option == 'No':
       break
