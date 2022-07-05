#recibe un numero entero y evalua si es negativo si lo es lo devuelve positivo.
def fn_num_pos(rec_num): # rec_num = received number, numero recivido.
    if rec_num < 0:
        rec_num *= -1
        return rec_num
    else:
        return rec_num

#recibe un numero entero y regresa la cantidad de digitos que componen el numero.
def fn_cont_dig(rec_num):
    cont = 0
    while rec_num != 0:
        rec_num = int(rec_num/10)
        cont += 1
    return cont

#recibe un numero entero y regresa su penultimo y ultimo digito
def fn_pen_ult_dig(rec_num):
    ult_dig = int(rec_num % 10)
    rec_num /= 10
    pen_dig = int(rec_num % 10)
    return [pen_dig, ult_dig]

#recibe un numero entero y regresa 0 si es par de lo contrario regresa 1 si no lo es.
def fn_num_par(rec_num):
    if int(rec_num / 2) * 2 == rec_num:
        return 0
    else:
        return 1

#recibe un numero entero y regresa una lista (vector) con los digitos separados en el mismo orden del numero ingresado.
def fn_digitos(rec_num):
    vec = []
    while rec_num != 0:
        vec.append(rec_num % 10)
        rec_num = int(rec_num / 10)
    vec.reverse()
    
    return vec