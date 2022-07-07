#la computadora adivinara el numero que el usuario ingrese
#The computer will guess the number that the user type.

from operator import or_
import random

def pcGuessNum(num_lim):
    while(True):
        ran_num = random.randint(1, num_lim)
        print("Digite un numero entero entre 1 y",num_lim,"para que la pc adivine el numero")
        print("Type an integer number among 1 and",num_lim,"the pc will guess the number")
        print("¿Desea salir? digite el numero 0\nDo you want to exit? type the number 0")
        try:
            num_usr = int(input(": "))
            if num_usr == 0:
                raise ZeroDivisionError
        except ValueError:
            print("Digite solo numeros\nType just numbers")
        except ZeroDivisionError:
            break
        else:
            while ran_num != num_usr:
                print("La pc tomo el numero",ran_num)
                print("El numero tomado por la pc es ¿menor o mayor?, si es menor escriba 'm' si es mayor escriba 'M'")
                men_may = input(": ")
                while not (men_may == "m" or men_may == "M"):
                        print("La pc tomo el numero",ran_num)
                        print("por favor escriba 'm' si el numero tomado por la pc es menor o 'M' si es mayor")
                        men_may = input(": ")

                if men_may == "m":
                    ran_num += 1
                elif men_may == "M":
                    ran_num -= 1
            print("La computadora ha adivinado el numero, es:",num_usr)

pcGuessNum(10)