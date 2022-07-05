#recibe un numero entero, regresa 1 si el numero es primo, 0 si no lo es.
# rec_num = received number, numero recibido.
def fn_num_primo(rec_num):
    ind=2
    sw=1
    if rec_num == 1:
        return 0
    else:
        while ind <= int(rec_num / 2) and sw == 1:
            if int(rec_num / ind) * ind == rec_num:
                sw = 0
            ind += 1
        return sw

#recibe dos numeros enteros (A, B) y regresa 0 si A es multiplo de B por el contrario retorna 1. A debe ser mayor que B.
def fn_num_mult(dig_a, dig_b):
    if dig_a % dig_b == 0:
        return 0
    else:
        return 1



#Recibe dos numeros enteros y retorna el resultado de la suma entre ellos.
def fn_suma(dig_a, dig_b):
    return dig_a + dig_b
