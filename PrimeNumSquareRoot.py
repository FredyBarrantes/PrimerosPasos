#El factor de un numero ocurre en pares, se puede correr hasta la raiz cuadrada de "n", este algoritmo es muy eficiente.
#As factors of a number occur in pairs, you can run only up to √n. This algorithm is a lot faster

import math

def fn_RootPrime(n):
    raiz = math.sqrt(n)
    print("la raiz es",raiz)
    for ind in range(2, int(math.sqrt(n))+1):
        print("indice",ind)
        if (n%ind) == 0:
            return print("El numero",n,"No es primo.")
    return print("El numero",n,"Es primo")

fn_RootPrime(997)