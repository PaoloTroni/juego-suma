import time


def probar_suma_dos_numeros(num1, num2):

    res_suma = num1 + num2
    user_res = int(input(f"\n{num1} + {num2} ES ?: "))
    print()
    if res_suma == user_res:
        print("MUY BIEN, REBECCA 🤪🎊🎉")
        print(f"{num1} + {num2}  ES {res_suma}.\n")
    else:
        print("MAL, REBECCA 🧐😩😭")
        print(f"{num1} + {num2}  ES {res_suma}.\n")


print("\nHOLA REBECCA \n")
while True:

    num1 = int(input("\nNUMERO, REBECCA: "))

    num2 = int(input("\nOTRO NUMERO, REBECCA: "))
    probar_suma_dos_numeros(num1, num2)

    print("----------------------------------------------------------------")

    time.sleep(4)
