 # szam = int(input("Adj meg egy számot 5-10 között: "))
 # while not 5 <= szam <=10:
 #   print(szam)
 # szam = int(input("Helytelen érték. Adj me egy másik számot!"))


szam = int(input("Adj megy egy számot: "))
helyes = 4
while helyes not in szam:
    print("Nem egyezik a szám.")
    if szam == 4:
       print("Kitaláltad a számot!")
    break