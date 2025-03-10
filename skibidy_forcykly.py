# # for i in range(3):
# #     print("Knock")
# # print("Penny!")


# # for i in range(1, 31):
# #     print(i, end = ' ')

# # for i in range(1, 33, 2):
# #     print(i, end = ' ')


# # slovo = "Ahoj já jsem forcyklus"
# # for znak in slovo:
# #    print(znak)


# # for i in range(1, 11):
# #     print(i, end = " ")
# # print()
# # for i in range(1, 11):
# #     print(i * 2, end = " ")
# # print()
# # for i in range(1, 11):
# #     print(i * 3, end = " ")
# # print()
# # for i in range(1, 11):
# #     print(i * 4, end = " ")
# # print()
# # for i in range(1, 11):
# #     print(i * 5, end = " ")
# # print()
# # for i in range(1, 11):
# #     print(i * 6, end = " ")
# # print()
# # for i in range(1, 11):
# #     print(i * 7, end = " ")
# # print()
# # for i in range(1, 11):
# #     print(i * 8, end = " ")
# # print()
# # for i in range(1, 11):
# #     print(i * 9, end = " ")
# # print()
# # for i in range(1, 11):
# #     print(i * 10, end = " ")



# # print("Malá násobilka pomocí dvou cyklů:")
# # for j in range(1, 11):
# #     for i in range(1, 11):
# #         print(i * j, end = " ")
# #     print()


# import random
# nahodne_cislo = random.randint(0, 100)
# pokusy = 0
# print("Vítej ve Hře Uhodni číslo")
# print("Zkus uhodnout mé číslo ;-)")
# print("PS: Číslo je v Rozsahu 0 - 100")
# print("Hodně Štěstí")

# while True:
#     hadane_cislo = float(input("Tvůj Tip: "))
#     pokusy += 1
#     if hadane_cislo != nahodne_cislo:
#         if hadane_cislo > nahodne_cislo:
#             print("Mé Číslo je Menší")
        
#         if hadane_cislo < nahodne_cislo:
#             print("Mé číslo je Větší")
    
#     if hadane_cislo == nahodne_cislo:
#         print("Bezva uhodl jsi mé číslo. Uhodl jsi ho na" ,pokusy, "pokusů")
#         print("Dobrá Práce :-)")
#         break

