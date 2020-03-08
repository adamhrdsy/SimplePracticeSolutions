dict = {1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-',9:'-'}
won = 0
elozo = 1
list = []
kerdesx = input("Ki lesz az X-el?: ")
kerdeso = input("Ki lesz a Kör-el?: ")
while True:
    def checker():
        global won
        if dict[list[0]] == "X" and dict[list[1]] == "X" and dict[list[2]] == "X":
            print(f"{kerdesx} - Megnyerte a játékot!!!!")
            won = 1
        elif dict[list[0]] == "O" and dict[list[1]] == "O" and dict[list[2]] == "O":
            print(f"{kerdeso} - Megnyerte a játékot!!!!")
            won = 1
        list.clear()
    print(dict[(1)], dict[(2)], dict[(3)])
    print(dict[(4)], dict[(5)], dict[(6)])
    print(dict[(7)], dict[(8)], dict[(9)])

    if won == 1:
        break

    if elozo == 1:
        mit = "O"
        elozo = 0
    else:
        mit = "X"
        elozo = 1

    while True:
        hova = int(input("Melyik mezőbe szeretnél írni?: "))

        if dict[hova] == '-':
            dict[hova] = mit
            break
        else:
            print("Már lett ebbe a mezőba irva")

    for y in range(1,4):
        for x in range(0,10)[y:10:3]:
            list.append(x)
        checker()

    for z in [0,3,6]:
        for s in range(1,4):
            list.append(s+z)
        checker()

    for k in range(1,11)[::4]:
        list.append(k)
    checker()

    for o in range(3,8)[::2]:
        list.append(o)
    checker()