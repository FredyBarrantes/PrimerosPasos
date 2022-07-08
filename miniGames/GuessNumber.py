#Adivina el numero / Guess the number
#El usuario debe adivinar un numero en un rango especifico generado aleatoriamente, el programa debe informar si el numero que el usuario ingreso
#es mayor, menor o igual al numero generado aleatoriamente.
#User should guess a number in an especific range generated randomly, the app will show if the number that the user typed is largest, lower
#and equal to the number randomly generated.

import random

ale_num = random.randint(1, 10)
while(True):
    print("////-////-////-////-////-////-////-////-////-////-////-////-////-////-////-////")
    print("Digite un numero entero entre 1 y 10\nType an integer number between 1 and 10")
    try:
        num_usr = int(input(": "))
        print("////-////-////-////-////-////-////-////-////-////-////-////-////-////-////-////")
        if num_usr == 0:
            raise ZeroDivisionError
    except ValueError:
        print("////-////-////-////-////-////-////-////-////-////-////-////-////-////-////-////")
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
        print("////-////-////-////-////-////-////-////-////-////-////-////-////-////-////-////")
    except ZeroDivisionError:
        break
    if num_usr > ale_num:
        print("////-////-////-////-////-////-////-////-////-////-////-////-////-////-////-////")
        print("El numero",num_usr,"es mayor\nNumber",num_usr,"is largest")
        print("////-////-////-////-////-////-////-////-////-////-////-////-////-////-////-////")
    elif num_usr < ale_num:
        print("////-////-////-////-////-////-////-////-////-////-////-////-////-////-////-////")
        print("El numero",num_usr,"es menor\nNumber",num_usr,"is lower")
        print("////-////-////-////-////-////-////-////-////-////-////-////-////-////-////-////")
    else:
        print("////-////-////-////-////-////-////-////-////-////-////-////-////-////-////-////")
        print("el numero aleatorio es",ale_num,"Adivinaste!!!")
        print("The random number is",ale_num,"you've guessed!!!")
        print("////-////-////-////-////-////-////-////-////-////-////-////-////-////-////-////")
        break