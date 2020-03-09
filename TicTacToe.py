# won = 0
# elozo = 1
# list = []
# tie_list = []
# dict = {}
#
# for i in range(1,10):
#     dict[i] = "-"
#
# kerdesx = input("Who's gonna go with X?: ")
# kerdeso = input("Who's gonna go with O?: ")
#
# while True:
#     def checker():
#         global won
#
#         if dict[list[0]] == dict[list[1]] == dict[list[2]] == "X":
#             print(f"{kerdesx} - won the game!!!!")
#             won = 1
#         elif dict[list[0]] == dict[list[1]] == dict[list[2]] == "O":
#             print(f"{kerdeso} - won the game!!!!")
#             won = 1
#         list.clear()
#
#     for pr in [0,3,6]:
#         print(dict[(1+pr)], dict[(2+pr)], dict[(3+pr)])
#
#     if won == 1:
#         break
#
#     for tie in dict.values():
#         tie_list.append(tie)
#     if not tie_list.__contains__("-"):
#         print("Tie")
#         break
#     tie_list.clear()
#
#     if elozo == 1:
#         mit = "O"
#         elozo = 0
#     else:
#         mit = "X"
#         elozo = 1
#
#     while True:
#         while True:
#             try:
#                 hova = int(input("Which field do you want to write in?: "))
#                 break
#             except ValueError:
#                 print("You did not gave any data to work with")
#
#         if hova >= 10 or hova == 0:
#             print("You can only use data between 1 and 9!")
#         elif dict[hova] == '-':
#             dict[hova] = mit
#             break
#         else:
#             print("That field is not empty")
#
#     for y in range(1,4):
#         for x in range(0,10)[y:10:3]:
#             list.append(x)
#         checker()
#
#     for z in [0,3,6]:
#         for s in range(1,4):
#             list.append(s+z)
#         checker()
#
#     for k in range(1,11)[::4]:
#         list.append(k)
#     checker()
#
#     for o in range(3,8)[::2]:
#         list.append(o)
#     checker()