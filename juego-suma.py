import time

nombre_jugador = "jugador"


def probar_suma_dos_numeros(num1, num2):

    res_suma = num1 + num2
    user_res = int(input(f"\n{num1} + {num2} ES ?: "))
    print()
    if res_suma == user_res:
        print(f"MUY BIEN, {nombre_jugador} 🤪🎊🎉")
        print(f"{num1} + {num2}  ES {res_suma}.\n")
    else:
        print(f"MAL, {nombre_jugador} 🧐😩😭")
        print(f"{num1} + {num2}  ES {res_suma}.\n")


print(f"\nHOLA {nombre_jugador} \n")
while True:

    num1 = int(input(f"\nNUMERO, {nombre_jugador}: "))

    num2 = int(input(f"\nOTRO NUMERO, {nombre_jugador}: "))
    probar_suma_dos_numeros(num1, num2)

    print("----------------------------------------------------------------")

    time.sleep(4)
