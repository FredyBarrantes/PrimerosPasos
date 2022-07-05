#Coding standard
#name a variable, exp: user_num
#name a function, exp: fn_ult_dig
#name class, exp: CnameClass
#name moduls or packages, exp: Name_Module

"""1. Construir una función que reciba una matriz 5x5 (2x2) y retorne la cantidad de veces que se repite su moda.
def moda(M):
    num = 0
    cont = 0
    save_cont = 0
    #se inician dos ciclos "for" el primero ingresa a la matriz y el segundo a la posicion dentro de la matriz.
    for fil in M:
        for col in fil:
            #"num" esta variable guarda el dato que se encuentre en la posicion 0 de la matriz. aumenta en uno cada iteracion.
            num = col
            #"cont" esta variable guarda cuantas veces se encuentra un numero de si mismo "moda".
            cont = 0
            #Estos dos ciclos toman el dato dentro de las listas que estan en la matriz.
            for f in M:
                for c in f:
                    #el dato anteriormente mensionado se compara con "num" si es igual "cont" aumenta en uno.
                    if num == c:
                        cont += 1
            #al terminar la iteracion de los dos ultimos ciclos compara si "cont" es mayor que "save_cont" quiere decir que el numero
            #guardado es menor al numero de veces que se encontro el numero.
            if cont > save_cont:
                save_cont = cont
                #"save_num" guarda el numero que se repite mas veces.
                save_num = num
    #regresa el numero que se repitio mas veces y cuantas veces.
    return [save_num, save_cont]


#MAIN (PRINCIPAL)
while(True):
    #se crea una lista y dentro de ella todas las listas que se quierean para crear la matriz.
    Matriz = [[], []]
    #"tam" en esta variable se indica cuantas "columnas" tendra la matriz.
    tam = 2
    cont = 0
    print("---------------------------------------------------------------")
    print("Esta aplicacion muestra cuantas veces se repite un numero en un conjunto.")
    print("This app shows how many times is a number among a group.")
    try:
        for ind in range(tam):
            print("Desea salir? escriba 0\nDo you want to exit? type 0.")
            print("Digite el",cont + 1,"numero.")
            col_a = int(input(": "))
            if col_a == 0:
                #Esta excepcion se lanza intencionalmente para que cuando el usuario digite el numero "0" salga del ciclo "for" se dirija
                #a la "exception" ZeroDivisionError y "rompa" el programa.
                raise ZeroDivisionError
            print("Desea salir? escriba 0\nDo you want to exit? type 0.")
            print("Digite el",cont + 2,"numero.")
            col_b = int(input(": "))
            if col_b == 0:
                raise ZeroDivisionError
            #Se envia las variables "col_a" y "col_b" a la matriz, dentro de esta se indica que "escriba" en la posicion 0, en esta posicion
            #se encuentra la primer lista, en la posicion 1 esta la otra lista.
            Matriz[0].append(col_a)
            Matriz[1].append(col_b)
            cont += 2
       
    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    except ZeroDivisionError:
        break

    else:
        #Se envia la matriz a la funcion "moda", esta regresa en una lista el numero que mas veces se repitio y la cantidad de veces 
        # que se repitio
        vec = moda(Matriz)
        print("EL numero",vec[0],"se repite",vec[1] - 1,"veces.")"""

#-------------------------------------------------------------+-----------------------------------------------------------------------
"""2. Construir una función que reciba como parámetro una matriz 4x4 entera y retorne la posición exacta en donde se encuentre almacenado
el mayor número primo.
import Funs_Mat

def may_num_primo(m):
    #"dat_mat" dato que se encuentra en la matriz.
    prim_may = 0
    dat_mat = 0
    pos_fil = -1
    pos_fil_may_pri = 0
    pos_col_may_pri = 0
    for fil_a in m:
        pos_fil += 1
        pos_col = -1
        for col_a in fil_a:
            pos_col +=1
            dat_mat_a = col_a
            if Funs_Mat.fn_num_primo(dat_mat_a) == 1:
                for fil_b in m:
                    for col_b in fil_b:
                        dat_mat_b = col_b
                        if Funs_Mat.fn_num_primo(dat_mat_b) == 1:
                            if dat_mat_a > dat_mat_b:
                                if dat_mat_a > prim_may:
                                    prim_may = dat_mat_a
                                    pos_fil_may_pri = pos_fil
                                    pos_col_may_pri = pos_col
    return [pos_fil_may_pri, pos_col_may_pri, prim_may]
                                                



while(True):
    Matriz = [[], []]
    tam = 2
    cont = 0
    print("---------------------------------------------------------------")
    print("Esta aplicacion muestra la posicion donde esta el mayor numero primo.")
    print("This app shows the position where is the largest prime number.")
    try:
        for ind in range(tam):
            print("Desea salir? escriba 0\nDo you want to exit? type 0.")
            print("Digite el",cont + 1,"numero.")
            col_a = int(input(": "))
            if col_a == 0:
                raise ZeroDivisionError
            print("Desea salir? escriba 0\nDo you want to exit? type 0.")
            print("Digite el",cont + 2,"numero.")
            col_b = int(input(": "))
            if col_b == 0:
                raise ZeroDivisionError
            Matriz[0].append(col_a)
            Matriz[1].append(col_b)
            cont += 2
    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    except ZeroDivisionError:
        break

    else:
        vec = may_num_primo(Matriz)
        fil = vec[0]
        col = vec[1]
        dat = vec[2]
        print("El mayor numero primo es:",dat,"se encuentra en el vector principal posicion",fil,"en el vector interno posicion",col)"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""3. Construir una función que reciba como parámetro un vector de 4 posiciones enteras y un dígito y que retorne la cantidad de números
del vector en donde dicho dígito está de penúltimo.

from package.Funs_Logic import fn_pen_ult_dig, fn_num_pos

def dig_es_penult(vec, dig):
    dat_vec = 0
    cont = 0
    for ind in vec:
        dat_vec = ind
        vec_pen_ult_dig = fn_pen_ult_dig(dat_vec)
        if dig == vec_pen_ult_dig[0]:
            cont += 1
    return cont

while(True):
    vec = []
    tam = 4
    cont = 0
    cant = 0
    print("Esta aplicacion muestra la cantidad de numeros en donde un digito esta de penultimo\nThis application shows the amount of numbers where a digit is penultimate")
    try:
        for ind in range(tam):
            cont += 1
            print("Desea salir? escriba 0\nDo you want to exit? type 0.")
            print("Digite un numero para la posicion",cont,":")
            print("Type a number to the position",cont,": ")
            num = int(input(": "))
            if num == 0:
                raise ZeroDivisionError
            num = fn_num_pos(num)
            vec.append(num)
        print("Escriba el digito:\nType a digit")
        dig = int(input())
        dig = fn_num_pos(dig)
        if dig == 0:
            raise ZeroDivisionError

    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    except ZeroDivisionError:
        break

    else:
        cant = dig_es_penult(vec, dig)
        print("El digitos",dig,"se encuentra como penultimo digito",cant,"veces.")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""4. Construir una función que reciba como parámetro un vector de 4 posiciones enteras y retorne la cantidad de números primos almacenados en el 
vector.

import Funs_Mat
from package.Funs_Logic import fn_num_pos

def cant_num_primo_vec(vec):
    cant = 0
    for ind in vec:
        dat_vec = ind
        if Funs_Mat.fn_num_primo(dat_vec) == 1:
            cant += 1
    return cant

while(True):
    vec = []
    tam = 4
    cont = 0
    cant = 0
    print("Esta aplicacion muestra cuantos numeros primos estan en el vector\nThis app shows how many prime numbers there are in the list")
    try:
        for ind in range(tam):
            cont += 1
            print("Desea salir? escriba 0\nDo you want to exit? type 0.")
            print("Digite un numero para la posicion",cont,":")
            print("Type a number to the position",cont,": ")
            num = int(input(": "))
            if num == 0:
                raise ZeroDivisionError
            num = fn_num_pos(num)
            vec.append(num)

    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    except ZeroDivisionError:
        break

    else:
        cant = cant_num_primo_vec(vec)
        print("la cantidad de numeros primos que estan en la lista son",cant)
        print("---------------------------------------+------------------------------------")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""5. Construir una función que reciba como parámetro un vector de 4 posiciones enteras y retorne el promedio entero del vector.

from package.Funs_Logic import fn_num_pos

def fn_prom_vec(vec):
    sum = 0
    for ind in vec:
        sum = ind + sum
    return sum // len(vec)

while(True):
    vec = []
    tam = 4
    cont = 0
    print("Esta aplicacion muestra el promedio entre numeros que esta nen una lista\nThis app shows the average between numbers that are in a list")
    try:
        for ind in range(tam):
            cont += 1
            print("Desea salir? escriba 0\nDo you want to exit? type 0.")
            print("Digite un numero para la posicion",cont,":")
            print("Type a number to the position",cont,": ")
            num = int(input(": "))
            if num == 0:
                raise ZeroDivisionError
            num = fn_num_pos(num)
            vec.append(num)

    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    except ZeroDivisionError:
        break

    else:
        promedio = fn_prom_vec(vec)
        print("El promedio de los numeros ingresados es",promedio)
        print("The average of the numbers typed is",promedio)
        print("---------------------------------------+------------------------------------")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""6. Construir una función que reciba como parámetro un entero y retorne 1 si dicho valor es un número de mínimo 3 dígitos. Deberá retornar 0 
si no es así.

from package.Funs_Logic import fn_num_pos, fn_cont_dig

def fn_tres_dig(num):
    if fn_cont_dig(num) == 3:
        return 1
    else:
        return 0

while(True):
    cant = 0
    print("Esta aplicacion regresa 1 si el numero ingresado tiene 3 digitos de lo contrario regresa 0")
    print("This app return 1 if the number typed has 3 digits if not return 0")
    print("Desea salir? escriba 0\nDo you want to exit? type 0.")
    try:
        num = int(input("Escriba un numero entero: "))
        num = fn_num_pos(num)
        if num == 0:
            raise ZeroDivisionError

    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    except ZeroDivisionError:
        break

    else:
        cant = fn_tres_dig(num)
        if cant == 1:
            print("El numero",num,"tiene tres digitos.")
            print("Number",num,"has three digits.")
            print("---------------------------------------+------------------------------------")
        else:
            print("El numero",num,"No tiene tres digitos.")
            print("Number",num,"Doesn't have three digits.")
            print("---------------------------------------+------------------------------------")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""7. Construir una función que reciba como parámetro una matriz 2x2 entera y retorne el número de la fila en donde se encuentre por primera vez
el número mayor de la matriz.

from package.Funs_Logic import fn_num_pos

def fn_fil_num_may_mat(matr):
    may_fil = 0
    num_may = 0
    cont_fil = -1
    for fil in matr:
        for col in fil:
            for line in matr:
                for column in line:
                    if col > column:
                        if col > num_may:
                            num_may = col
    
    for fil in matr:
        cont_fil += 1
        for col in fil:
            if num_may == col:
                return cont_fil

while(True):
    mat = [[], []]
    cont = 0
    tam = 2
    print("Esta aplicacion muestra la fila donde se encuentra por primera vez el numero mayor.")
    print("This app shows the line where is find for the first time the longest number")
    print("Desea salir? escriba 0\nDo you want to exit? type 0.")
    try:
        for ind in range(tam):
            cont +=1
            print("Digite un numero entero para la columna",cont)
            num_a = int(input(": "))
            num_a = fn_num_pos(num_a)
            if num_a == 0:
                raise ZeroDivisionError
            print("Digite un numero entero para la columna",cont +1)
            num_b = int(input(": "))
            num_b = fn_num_pos(num_b)
            if num_b == 0:
                raise ZeroDivisionError
            mat[0].append(num_a)
            mat[1].append(num_b)
            cont -=1

    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    except ZeroDivisionError:
        break

    else:
        num_fil = fn_fil_num_may_mat(mat)
        print("La fila donde se encuentra por primera vez el numero mayor es:",num_fil)
        print("The line where is find for the first time the longest number is:",num_fil)
        print("---------------------------------------+------------------------------------")"""
#-------------------------------------------------------------+-----------------------------------------------------------------------
"""8. Construir una función que reciba como parámetro una matriz de 3x2 entera y retorne la cantidad de veces que se repite el mayor dato
de la matriz."""

from package.Funs_Logic import fn_num_pos

def cant_may_dat_mat(mat):
    may_dat = 0
    cant = 0
    for line in mat:
        for colm in line:
            for fil in mat:
                for col in fil:
                    if colm > col:
                        if colm > may_dat:
                            may_dat = colm
    
    for fil in mat:
        for col in fil:
            if may_dat == col:
                cant +=1
    return cant

while(True):
    mat = [[], [], []]
    fila = 2
    cont = -1
    print("Esta aplicacion muestra la cantidad de veces que se repite el mayor dato en una matriz")
    print("This app shows the amount of times that is repeted the biggest data in a matrix")
    print("Desea salir? escriba 0\nDo you want to exit? type 0.")
    try:
        for ind in range(fila):
            cont +=1
            print("Digite un numero entero para la columna",cont)
            print("Type an integer number to add the column",cont)
            num_a = int(input(": "))
            num_a = fn_num_pos(num_a)
            if num_a == 0:
                raise ZeroDivisionError
            print("Digite un numero entero para la columna",cont + 1)
            print("Type an integer number to add the column",cont + 1)
            num_b = int(input(": "))
            num_b = fn_num_pos(num_b)
            if num_b == 0:
                raise ZeroDivisionError
            print("Digite un numero entero para la columna",cont + 2)
            print("Type an integer number to add the column",cont + 2)
            num_c = int(input(": "))
            num_c = fn_num_pos(num_c)
            if num_c == 0:
                raise ZeroDivisionError
            mat[0].append(num_a)
            mat[1].append(num_b)
            mat[2].append(num_c)
    except ValueError:
        print("Por favor ingrese solo numeros.")
        print("Please type just numbers.")
    except ZeroDivisionError:
        break

    else:
        cant = cant_may_dat_mat(mat)
        print("El numero mayor de la matriz esta",cant,"veces.")
        print("Matrix's number largest is",cant,"times.")
        print("---------------------------------------+------------------------------------")