#Coding standard
#name a variable, exp: user_num
#name a function, exp: fn_ult_dig
#name class, exp: CnameClass
#name moduls or packages, exp: Name_Module

"""1. construir una funcion que reciba como parametro un entero y retorne su ultimo digito.
from package.Funs_Logic import fn_num_pos, fn_pen_ult_dig
while(True):
    print("Este programa muestra el ultimo digito del numero ingresado\nThis app shows the last digit of the received number")
    try:
        user_num = int(input("Escriba un numero entero. Para terminar escriba cualquier letra\nType an integer number. To finish the app type any letter: "))
    except ValueError:
        print("Hasta pronto\nSee you")
        break
    else:
        user_num = fn_num_pos(user_num)
        ult_dig = fn_pen_ult_dig(user_num)
        print("El ultimo digito del numero",user_num,"es",ult_dig[1])
        print("The las digit of the number",user_num,"es",ult_dig[1])"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""2. construir una funcion que reciba como parametro un entero y retorne sus dos ultimos digitos.
from package.Funs_Logic import fn_num_pos, fn_cont_dig, fn_pen_ult_dig
var_exit = "0"
while(True):
    print("Este programa muestra los dos ultimos digitos de un numero.\nThis app shows the las two digits of a number.")
    try:
        print("-----------------------------------------------------------------")
        user_num = int(input("Escriba un numero entero\nType an integer number: "))
    except ValueError:
        print("-----------------------------------------------------------------------------------------------------------")
        print("Desea salir? escriba E. Para continuar oprima enter\nDo you want to exit? type E. To continue press enter: ")
        var_exit = input()
        if var_exit == "E":
            break
    else:
        user_num = fn_num_pos(user_num)
        can_dig = fn_cont_dig(user_num)
        if can_dig >= 2:
            tup = fn_pen_ult_dig(user_num)
            print("Los dos ultimos digitos del numero",user_num,"son",tup[0],"y",tup[1])
            print("The last two digits of the number",user_num,"are",tup[0],"and",tup[1])
            print("--------------------------------------------------------------------")
        else:
            print("El numero",user_num,"tienen menos de dos digitos.")
            print("Number",user_num,"has less than two digits.")
            print("-------------------------------------------------")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""3. construir una funcion que reciba como parametro un entero y retorne la cantidad de digitos.
from package.Funs_Logic import fn_cont_dig
var_exit = "0"
while(True):
    print("----------------------------------------------------------------------------------------------------")
    print("Este programa muestra cuantos digitos tiene un numero.\nThis app shows how many digits has a number.")
    try:
        print("------------------------------------------------------------------")
        user_num = int(input("Escriba un numero entero:\nType an integer number: "))
    except ValueError:
        print("Desea salir? escriba 'salir'. Para continuar oprima enter:\nDo you want to exit? type 'exit'. To continue press enter: ")
        var_exit = input()
        if var_exit == "salir" or "exit":
            break
    else:
        can_dig = fn_cont_dig(user_num)
        print("la cantidad de digitos del numero",user_num,"son",can_dig)
        print("the amount of digits of the number",user_num,"are",can_dig)"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""4. Leer un número entero de dos dígitos y determinar a cuánto es igual la suma de sus dígitos.
import Funs_Mat
from package.Funs_Logic import fn_num_pos, fn_cont_dig, fn_pen_ult_dig
while(True):
    print("----------------------------------------------------------")
    print("Este programa muestra la suma de los digitos de un numero.\nThis app shows the addition among the digits of a number.")
    try:
        print("------------------------------------------------------")
        user_num = int(input("Escriba un numero entero:\nType an integer number: "))
    except ValueError:
        print("Desea salir? escriba 'salir'. Para continuar oprima enter:\nDo you want to exit? type 'exit'. To continue press enter: ")
        var_exit = input()
        if var_exit == "salir" or "exit":
            break
    else:
        user_num = fn_num_pos(user_num)
        can_dig = fn_cont_dig(user_num)
        if can_dig == 2:
            tup = fn_pen_ult_dig(user_num)
            result = Funs_Mat.fn_suma(tup[0], tup[1])
            print("la suma de los digitos del numero",user_num,"es:",result)
            print("The addition of the digits of number",user_num,"is:",result)
        else:
            print("-------------------------------------------------------------------------------------")
            print("El numero",user_num,"no tiene dos digitos, por favor escriba un entero de dos digitos")
            print("Number",user_num,"doesn't have two digits, please type an integer of two digits.")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""5. Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.
from package.Funs_Logic import fn_num_par, fn_cont_dig, fn_pen_ult_dig

while(True):
    print("----------------------------------------------------------")
    print("Este programa muestra si los dos digitos del numero son pares\nThis app shows if the two digits of the number are even numbers.")
    try:
        print("------------------------------------------------------")
        user_num = int(input("Escriba un numero entero:\nType an integer number: "))
    except ValueError:
        print("Desea salir? escriba 'salir'. Para continuar oprima enter:\nDo you want to exit? type 'exit'. To continue press enter: ")
        var_exit = input()
        if var_exit == "salir" or "exit":
            break
    else:
        can_dig = fn_cont_dig(user_num)
        if can_dig == 2:
            tup = fn_pen_ult_dig(user_num)
            dig_a = fn_num_par(tup[0])
            dig_b = fn_num_par(tup[1])
            if dig_a == 0 and dig_b == 0:
                print("Los digitos del numero",user_num,"son pares.")
                print("The digits of number",user_num,"are even numbers.")
            elif dig_a == 1 and dig_b == 1:
                print("Los digitos del numero",user_num,"son impares.")
                print("The digits of number",user_num,"are odd numbers.")
            elif dig_a == 0 and dig_b == 1:
                print("El digito",tup[0],"es par, el digito",tup[1],"es impar.")
                print("The digit",tup[0],"is even number, the digit",tup[1],"is odd number.")
            elif dig_a == 1 and dig_b == 0:
                print("El digito",tup[0],"es impar, el digito",tup[1],"es par.")
                print("The digit",tup[0],"is odd number, the digit",tup[1],"is even number.")
        else:
            print("El numero ingresado no tiene dos digitos, ingrese un numero con dos digitos.")
            print("The number received doesn't have two digits, type a number with two digits.")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""6. Leer un número entero de dos dígitos menor que 20 y determinar si es primo.
from package.Funs_Logic import fn_num_pos, fn_cont_dig
import Funs_Mat
while(True):
    print("----------------------------------------------------------")
    print("Este programa comprueba que el numero tenga dos digitos, que sea menor a 20 y sea primo.")
    print("This app check that the number has two digits, less than 20 and be prime number.")
    try:
        print("------------------------------------------------------")
        user_num = int(input("Escriba un numero entero:\nType an integer number: "))
    except ValueError:
        print("Desea salir? escriba 'salir'. Para continuar oprima enter:\nDo you want to exit? type 'exit'. To continue press enter: ")
        var_exit = input()
        if var_exit == "salir" or "exit":
            break
    else:
        user_num = fn_num_pos(user_num)
        can_dig = fn_cont_dig(user_num)
        if can_dig == 2:
            if user_num < 20:
                if Funs_Mat.fn_num_primo(user_num) == 1:
                    print("El numero",user_num,"tiene dos digitos, es menor que 20 y es primo.")
                    print("The number",user_num,"has two digits, is less than 20 and is prime.")
                else:
                    print("El numero",user_num,"tiene dos digitos, es menor que 20 y NO es primo.")
                    print("The number",user_num,"has two digits, is less than 20 and is Not prime.")
            else:
                print("El numero",user_num,"es mayor a 20, ingrese un numero menor a 20.")
                print(""The number",user_num,"has two digits, is less than 20 and is prime."")
        else:
            print("EL numero",user_num,"no tiene dos digitos, ingrese un numero con solo dos digitos.")
            print("The number",user_num,"doesn't have two digits, type a number just with two digits.")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""7. Leer un número entero de dos dígitos y determinar si es primo y además si es negativo.Para desarrollar el ejercicio si el numero
es negativo volver lo positivo, establecer si es primo y si el usuario digito el numero negativo.
from package.Funs_Logic import fn_num_pos, fn_cont_dig
import Funs_Mat

while(True):
    print("----------------------------------------------------------")
    print("Este programa muestra si el numero es primo y ademas si el usuario originalmente digito un numero negativo")
    try:
        user_num = int(input("Escriba un numero entero:\nType an integer number: "))
    except ValueError:
        print("Desea salir? escriba 'salir'. Para continuar oprima enter:\nDo you want to exit? type 'exit'. To continue press enter: ")
        var_exit = input()
        if var_exit == "salir" or "exit":
            break
    else:
        neg_num = user_num
        user_num = fn_num_pos(user_num)
        can_dig = fn_cont_dig(user_num)
        if can_dig == 2:
            if Funs_Mat.fn_num_primo(user_num) == 1 and neg_num < 0:
                print("El numero ingresado",neg_num,"es primo y es negativo.")
                print("The received number",neg_num,"is prime and is negative.")
            elif Funs_Mat.fn_num_primo(user_num) == 0 and neg_num < 0:
                print("El numero ingresado",neg_num,"No es primo y es negativo.")
                print("The received number",neg_num,"is Not prime and is negative.")
            elif Funs_Mat.fn_num_primo(user_num) == 1 and neg_num > 0:
                print("El numero ingresado",neg_num,"es primo y es positivo.")
                print("The received number",neg_num,"is prime and is positive.")
            else:
                print("El numero ingresado",neg_num,"no es primo y es positivo")
                print("The received number",neg_num,"is not prime and is positive")
        else:
            print("El numero ingresado",neg_num,"no tiene dos digitos, escriba un numero de dos digitos.")
            print("The received number",neg_num,"doesn't have two digits, type a number with two digits.")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""8. Leer un número entero de dos dígitos y determinar si sus dos dígitos son primos.
import Funs_Mat
from package.Funs_Logic import fn_num_pos, fn_cont_dig, fn_pen_ult_dig

while(True):
    print("Este programa muestra si los dos digitos de un numero son primos")
    print("This app shows if two digits of a number are prime.")
    try:
        print("----------------------------------------------------------")
        user_num = int(input("Escriba un numero entero de DOS digitos.\nType an integer number of TWO digits: "))
    except ValueError:
        print("Desea salir? escriba 'salir'. Para continuar oprima enter:\nDo you want to exit? type 'exit'. To continue press enter: ")
        var_exit = input()
        if var_exit == "salir" or "exit":
            break
    else:
        user_num = fn_num_pos(user_num)
        if fn_cont_dig(user_num) == 2:
            tup = fn_pen_ult_dig(user_num)
            dig_a = Funs_Mat.fn_num_primo(tup[0])
            dig_b = Funs_Mat.fn_num_primo(tup[1])
            print(dig_a, dig_b, tup[0:])
            if dig_a and dig_b == 1:
                print("Ambos digitos del numero",user_num,"son primos.")
                print("Both digits of number",user_num,"are prime.")
                print("----------------------------------------------------------")
            elif dig_a == 0 and dig_b == 0:
                print("Los digitos del numero",user_num," No son primos.")
                print("The digits of number",user_num,"are Not prime.")
                print("----------------------------------------------------------")
            elif dig_a == 1 and dig_b == 0:
                print("El digito",tup[0],"es primo pero el digito",tup[1],"No es primo.")
                print("Digit",tup[0],"is prime but digit",tup[1],"is Not prime.")
                print("----------------------------------------------------------")
            else:
                print("El digito",tup[0],"No es primo pero el digito",tup[1],"es primo.")
                print("Digit",tup[0],"is Not prime but digit",tup[1],"is prime.")
                print("----------------------------------------------------------")
        else:
            print("Por favor digite un numero de DOS digitos.")
            print("Please type a number of TWO digits.")
            print("----------------------------------------------------------")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""9. Leer un número entero de dos dígitos y determinar si un dígito es múltiplo del otro.
import Funs_Mat
from package.Funs_Logic import fn_num_pos, fn_cont_dig, fn_pen_ult_dig

while(True):
    print("----------------------------------------------------------")
    print("Este programa muestra si un digito es multiplo del otro")
    print("This app shows if a digit is multiple of other one.")
    try:
        print("----------------------------------------------------------")
        user_num = int(input("Escriba un numero entero de DOS digitos.\nType an integer number of TWO digits: "))
    except ValueError:
        print("Desea salir? escriba 'salir'. Para continuar oprima enter:\nDo you want to exit? type 'exit'. To continue press enter: ")
        var_exit = input()
        if var_exit == "salir" or "exit":
            break
    else:
        user_num = fn_num_pos(user_num)
        if fn_cont_dig(user_num) == 2:
            tup = fn_pen_ult_dig(user_num)
            if tup[0] > tup[1]:
                if Funs_Mat.fn_num_mult(tup[0], tup[1]) == 0:
                    print("El digito",tup[0],"es multiplo del digito",tup[1])
                    print("Digit",tup[0],"is multiple of the digit",tup[1])
                else:
                    print("El digito",tup[0],"No es multiplo del digito",tup[1])
                    print("Digit",tup[0],"is Not multiple of the digit",tup[1])

            elif Funs_Mat.fn_num_mult(tup[1], tup[0]) == 0:
                    print("El digito",tup[1],"es multiplo del digito",tup[0])
                    print("Digit",tup[1],"is multiple of the digit",tup[0])
            else:
                    print("El digito",tup[1],"No es multiplo del digito",tup[0])
                    print("Digit",tup[1],"is Not multiple of the digit",tup[0])

        else:
            print("El numero",user_num,"debe tener DOS digitos.")
            print("The Number",user_num," must has TWO digits.")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""10. Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.
from package.Funs_Logic import fn_num_pos, fn_cont_dig, fn_pen_ult_dig

while(True):
    print("----------------------------------------------------------")
    print("Este programa muestra si los digitos de un numero son iguales.")
    print("This app shows if the digits of a number are equal.")
    try:
        print("----------------------------------------------------------")
        user_num = int(input("Escriba un numero entero de DOS digitos.\nType an integer number of TWO digits: "))
    except ValueError:
        print("Desea salir? escriba 'salir'. Para continuar oprima enter:\nDo you want to exit? type 'exit'. To continue press enter: ")
        var_exit = input()
        if var_exit == "salir" or "exit":
            break
    else:
        user_num = fn_num_pos(user_num)
        if fn_cont_dig(user_num) == 2:
            tup = fn_pen_ult_dig(user_num)
            if tup[0] == tup[1]:
                print("Los digitos son iguales.")
            else:
                print("Los digitos son diferentes.")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""11. Leer dos números enteros y determinar cuál es el mayor.

while(True):
    print("----------------------------------------------------------")
    print("Este programa muestra que numero es mayor entre dos numeros:")
    print("This app shows which number is largest within two number: ")
    try:
        print("----------------------------------------------------------")
        print("Desea salir? escriba 0\nDo you want to exit? type 0")
        user_num_a = int(input("Escriba el primer numero entero:\nType the first integer number: "))
        if user_num_a == 0:
            break
        user_num_b = int(input("Escriba el segundo numero entero:\nType the second integer number: "))
        if user_num_b == 0:
            break
    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    else:
        if user_num_a > user_num_b:
            print("el numero",user_num_a,"es mayor que el numero",user_num_b)
            print("The number",user_num_a,"is largest than the number",user_num_b)
        else:
            print("el numero",user_num_b,"es mayor que el numero",user_num_a)
            print("The number",user_num_b,"is largest than the number",user_num_a)"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""12. Leer dos números enteros de dos dígitos y determinar si tienen dígitos comunes.
from package.Funs_Logic import fn_num_pos, fn_cont_dig, fn_pen_ult_dig

while(True):
    print("----------------------------------------------------------")
    print("Este programa muestra si los digitos de dos numeros son comunes.")
    print("This app shows if the digits of two number are common numbers.")
    try:
        print("----------------------------------------------------------")
        print("Desea salir? escriba 0\nDo you want to exit? type 0")
        user_num_a = int(input("Escriba el primer numero de DOS digitos:\nType the first number of TWO digits: "))
        if user_num_a == 0:
            break
        user_num_b = int(input("Escriba el segundo numero de DOS digitos:\nType the second number of TWO digits: "))
        if user_num_b == 0:
            break
    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    else:
        user_num_a = fn_num_pos(user_num_a)
        user_num_b = fn_num_pos(user_num_b)
        if fn_cont_dig(user_num_a) == 2 and fn_cont_dig(user_num_b) == 2:
            vec_a = fn_pen_ult_dig(user_num_a)
            vec_b = fn_pen_ult_dig(user_num_b)
            cont = 0
            for i in vec_a:
                for e in vec_b:
                    if i == e:
                        print("El digito",i,"es comun.")
                        print("The digit",i,"is common.")
                        cont =+ 1
            if cont == 0:
                print("EL numero",user_num_a,"no tiene ningun digito comun con el numero",user_num_b)
                print("Number",user_num_a,"doesn't have any digit common with the number",user_num_b)
        else:
            print("Los numeros ingresados deben ser de DOS digitos.")
            print("The numbers typed must be of TWO digits.")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""13. Leer dos números enteros de dos dígitos y determinar si la suma de los dos números origina un número par.
from package.Funs_Logic import fn_num_pos, fn_cont_dig, fn_num_par

while(True):
    print("----------------------------------------------------------")
    print("Este programa muestra si la suma entre dos numeros genera un numero par.")
    print("This app shows if the addition between two number result an even number.")
    try:
        print("----------------------------------------------------------")
        print("Desea salir? escriba 0\nDo you want to exit? type 0")
        user_num_a = int(input("Escriba el primer numero de DOS digitos:\nType the first number of TWO digits: "))
        if user_num_a == 0:
            break
        user_num_b = int(input("Escriba el segundo numero de DOS digitos:\nType the second number of TWO digits: "))
        if user_num_b == 0:
            break
    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    else:
        user_num_a = fn_num_pos(user_num_a)
        user_num_b = fn_num_pos(user_num_b)
        if fn_cont_dig(user_num_a) == 2 and fn_cont_dig(user_num_b) == 2:
            if fn_num_par(user_num_a + user_num_b) == 0:
                print("El resultado de sumar",user_num_a,"y",user_num_b,"es par.")
                print("the answer of addition."user_num_a"and"user_num_b"is an even number")
            else:
                print("El resultado de sumar",user_num_a,"y",user_num_b,"NO es par.")
                print("The answer of addition."user_num_a"and"user_num_b"is Not an even number")
        else:
            print("Los numeros ingresados deben tener solo DOS digitos.")
            print("The numbers typed must be of TWO digits.")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""14. Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos los dígitos.
from package.Funs_Logic import fn_num_pos, fn_cont_dig, fn_pen_ult_dig
result = 0

while(True):
    print("----------------------------------------------------------")
    print("Este programa muestra la suma entre dos numeros.")
    print("This app shows the addition between two number.")
    try:
        print("----------------------------------------------------------")
        print("Desea salir? escriba 0\nDo you want to exit? type 0")
        user_num_a = int(input("Escriba el primer numero de DOS digitos:\nType the first number of TWO digits: "))
        if user_num_a == 0:
            break
        user_num_b = int(input("Escriba el segundo numero de DOS digitos:\nType the second number of TWO digits: "))
        if user_num_b == 0:
            break
    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    else:
        user_num_a = fn_num_pos(user_num_a)
        user_num_b = fn_num_pos(user_num_b)
        if fn_cont_dig(user_num_a) == 2 and fn_cont_dig(user_num_b) == 2:
            vec_a = fn_pen_ult_dig(user_num_a)
            vec_b= fn_pen_ult_dig(user_num_b)
            for i in vec_a:
                result += i
            for i in vec_b:
                result += i
            print("la suma entre los digitos de los numeros ingresados es:",result)
            print("The addition between the digits of numbers typed is:",result)   
        else:
            print("Por favor digite numeros solo de DOS digitos.")
            print("The numbers typed must be of TWO digits.")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""15. Leer un número entero de tres dígitos y determinar a cuánto es igual la suma de sus dígitos."""
           #la solucion es la misma que en el ejercicio anterior (N° 14). The solution is the same than the previous exercise (N° 14)

#-------------------------------------------------------------+-----------------------------------------------------------------------
"""16. Leer un número entero de tres dígitos y determinar si al menos dos de sus tres dígitos son iguales.
from package.Funs_Logic import fn_num_pos, fn_cont_dig, fn_digitos

while(True):
    print("----------------------------------------------------------")
    print("Este programa muestra si dos de los tres digitos de un numeros son iguales.")
    print("This app shows if two of the three digits of a number are equal.")
    try:
        print("----------------------------------------------------------")
        print("Desea salir? escriba 0\nDo you want to exit? type 0")
        user_num = int(input("Escriba un numero de tres digitos:\nType a number of three digits: "))
        if user_num == 0:
            break
    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    else:
        user_num  = fn_num_pos(user_num)
        if fn_cont_dig(user_num) == 3:
            vec = fn_digitos(user_num)
            cont = 0
            for i in vec:
                cont -= 1
                for e in vec:
                    if i == e:
                        cont += 1
            if cont == 2:
                print("El numero",user_num,", DOS de sus digitos son iguales.")
                print("Number",user_num,", TWO of its digits are equal.")
            elif cont > 2:
                print("El numero",user_num,", mas de DOS de sus digitos son iguales")
                print("Number",user_num,", more than TWO of its digits are equal..")
            else:
                print("El numero",user_num,", No tiene digitos iguales.")
                print("Number",user_num,", Doesn't have equal digits.")
        else:
            print("Por favor digite numeros solo de TRES digitos.")
            print("The numbers typed must be of THREE digits.")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""17. Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.
from package.Funs_Logic import fn_num_pos, fn_cont_dig, fn_digitos

while(True):
    print("----------------------------------------------------------")
    print("Este programa muestra en que posicion esta el mayor digito de un numero.")
    print("This app shows in which position is the largest digit of a number.")
    try:
        print("----------------------------------------------------------")
        print("Desea salir? escriba 0\nDo you want to exit? type 0")
        user_num = int(input("Escriba un numero de tres digitos:\nType a number of three digits: "))
        if user_num == 0:
            break
    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    else:
        user_num  = fn_num_pos(user_num)
        if fn_cont_dig(user_num) == 3:
            #se envia el numero a la funcion "fn_digitos", esta devuelve en un vector los digitos del numero.
            #send the number to the fuction "fn_digitos", this return in a list the digits of number.
            vec = fn_digitos(user_num)
            #la variable "pos" llevara la posicion en la que se encuentra "i"/ the variable "pos" keeps the position of "i".
            pos = 0
            #la variable "save_dig" guarda el digito mayor del numero/the variable "save_dig" keeps the largest digit of number.
            save_dig = 0
            #la variable "save_pos" guarda la posicion del digito mayor del numero/the variable "save_pos" keeps the position of the largest digit of number.
            save_pos = 0
            #Dos ciclos For uno anidado en el otro, sirven para comparar los digitos del numero entre si.
            #Two For loops one nested in the other, work to compare the digits of the number.
            for i in vec:
                #"pos" suma 1 para indicar que inicia en la posicion uno./"pos" addition 1 to shows that start in position one.
                pos += 1
                for e in vec:
                    if i > e:
                        #si "i" es mayor que "e" y si "i" es mayor a "save_dig", esta variable guarda la posicion de "i" en caso que ambas
                        # condiciones se cumplan actualiza la info en "save_pos" y "save_dig"
                        if i > save_dig:
                            save_pos = pos
                            save_dig = i
            #si "save_dig" y "save_pos" son iguales a cero que es el valor inicial de estas variables, quiere decir que no se encontro
            #ningun digito mayor por lo tanto todos los digitos son iguales.
            if save_dig == 0 and save_pos == 0:
                print("los tres disgitos del numero",user_num,"son iguales.")
            #si no quiere dicer que "save_dig" y "save_pos" son diferentes a cero, por lo tanto existe al menos un digito mayor a los otros.
            else:
                print("El digito",save_dig,"es el mayor y se encuentra en la posicion",save_pos)
        else:
            print("Por favor digite un numero solo de TRES digitos.")
            print("The number typed must be of THREE digits.")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""18. Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros.
from package.Funs_Logic import fn_num_pos, fn_cont_dig, fn_digitos
import Funs_Mat

while(True):
    print("----------------------------------------------------------")
    print("Este programa muestra si algun digito de un numero es multiplo de los otros digitos.")
    print("This app shows if some digit of a number is multiple of the other digits.")
    try:
        print("----------------------------------------------------------")
        print("Desea salir? escriba 0\nDo you want to exit? type 0")
        user_num = int(input("Escriba un numero de tres digitos:\nType a number of three digits: "))
        if user_num == 0:
            break
    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    else:
        user_num  = fn_num_pos(user_num)
        if fn_cont_dig(user_num) == 3:
            vec = fn_digitos(user_num)
            #la variable "sw" sirve como un "switch" para saber si se encontro un digithttps://www.w3schools.com/python/default.aspo multiplo de otro.
            #The variable "sw" works like a "switch" to know if found a multiple digit of other.
            sw = 0
            #La variable "pos_i" guarda la posicion en la que se encuentra "i", se inicia en 0.
            pos_i = 0
            for i in vec:
                #La variable "pos_e" guarda la posicion en la que se encuentra "e", se inicia en 0.
                pos_e = 0
                #"pos_i" aumenta en 1 asi guarda la posicion de "i".
                pos_i += 1
                for e in vec:
                    #"pos_e" aumenta en 1 asi guarda la posicion de "e".
                    pos_e += 1
                    #Si "pos_i" y "pos_e" son diferentes sigue, si no se estara comparando el mismo digito ya que ambas variables guardan la posicion.
                    if pos_i != pos_e:
                        if Funs_Mat.fn_num_mult(i, e) == 0:
                            print("El digito",i,"es multiplo del digito",e)
                            sw = 1
            if sw == 0:
                print("Ningun digito del numero",user_num,"es multiplo de otro digito.")
        else:
            print("Por favor digite un numero solo de TRES digitos.")
            print("The number typed must be of THREE digits.")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""19. Leer tres números enteros y determinar cuál es el mayor. Usar solamente dos variables.

while(True):
    print("----------------------------------------------------------")
    print("Este programa muestra que numero de tres es mayor.")
    print("This app shows which number of three is largest.")
    try:
        print("----------------------------------------------------------")
        print("Desea salir? escriba 0\nDo you want to exit? type 0")
        user_num_a = int(input("Escriba el primer numero:\nType the first number: "))
        if user_num_a == 0:
            break
        user_num_b = int(input("Escriba el segundo numero:\nType the second number: "))
        if user_num_b == 0:
            break
    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    else:
        if user_num_a > user_num_b:
            user_num_b = int(input("Escriba el tercer numero:\nType the third number: "))
            if user_num_a > user_num_b:
                print(user_num_a,"Es el numero mayor.")
            else:
                print(user_num_b,"Es el numero mayor.")
        else:
            user_num_a = int(input("Escriba el tercer numero:\nType the third number: "))
            if user_num_b > user_num_a:
                print(user_num_b,"Es el numero mayor.")
            else:
                print(user_num_a,"Es el numero mayor.")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""20. Leer tres números enteros y mostrarlos ascendentemente.

while(True):
    print("----------------------------------------------------------")
    print("Este programa muestra que numero de tres es mayor.")
    print("This app shows which number of three is largest.")
    try:
        print("----------------------------------------------------------")
        print("Desea salir? escriba 0\nDo you want to exit? type 0")
        user_num_a = int(input("Escriba el primer numero:\nType the first number: "))
        if user_num_a == 0:
            break
        user_num_b = int(input("Escriba el segundo numero:\nType the second number: "))
        if user_num_b == 0:
            break
        user_num_c = int(input("Escriba el tercer numero:\nType the second number: "))
        if user_num_c == 0:
            break
    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    else:
        men_num = 1000000
        may_num = 0
        med_num = 0
        vec = [user_num_a, user_num_b, user_num_c]

        #FORMA AUTOMATICA (usando la funcion sort)
        #vec.sort()
        #print(vec)

        #FORMA MANUAL
        #dos ciclos para comparar entre los mismos numeros quien es el menor y el mayor
        for i in vec:
            for e in vec:
                if i < e:
                    #"men_num" guarda el numero menor entre los tres numeros.
                    if i < men_num:
                        men_num = i
                elif i > e:
                    #"may_num" guarda el numero mayor entre los tres numeros.
                    if i > may_num:
                        may_num = i

        #este ciclo compara si es mayor al numero menor y si es menor al numero mayor quiere decir que es el numero medio.
        for i in vec:
            if i > men_num and i < may_num:
                med_num = i
        print(men_num, med_num, may_num)"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
