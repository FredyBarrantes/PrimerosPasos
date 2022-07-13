# Juego del ahorcado, el jugador debe adivinar la palabra diciendo las letras que cree que componen la palabra. El numero de errores son 
# siete (7).
#Text art para el juego fue descargado de: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c Agradecimientos al autor.


import random
import string
 
import HangmanAssets


def fn_errors(cont):
    if cont == 1:
        print("Primer error, preparada la horca.")
        print(HangmanAssets.text_art[0])
    elif cont == 2:
        print("Segundo error, verdugo traiga al sentenciado.")
        print(HangmanAssets.text_art[1])
    elif cont == 3:
        print("Tercer error, verdugo ponga la soga en el cuello.")
        print(HangmanAssets.text_art[2])
    elif cont == 4:
        print("Cuarto error, verdugo apriete la soga.")
        print(HangmanAssets.text_art[3])
    elif cont == 5:
        print("Quinto error, Ha sido sentenciado por no adivinar la palabra.")
        print(HangmanAssets.text_art[4])
    elif cont == 6:
        print("Sexto error, Verdugo preparece para jalar la palanca.")
        print(HangmanAssets.text_art[5])
    else:
        print("Ultimo error.")
        print(HangmanAssets.text_art[6])


def fn_juego_ahorcado():
    user_let = "B"
    cont = 0
    #Se escoge un palabra aleatoria de la lista "animales" que se encuentra en el archivo "HangmanAssets.py"
    palabra_aleatoria = random.choice(HangmanAssets.animales)
    #Se convierte la palabra entera a mayusculas.
    palabra_aleatoria = palabra_aleatoria.upper()
    #Se crea una coleccion "set" con el nombre "letras_adivinar", se ponen las letras separadas dentro de este conjunto.
    letras_adivinar = set(palabra_aleatoria)
    #En la variable "letras_digitadas" se guardaran las letras que el jugador digite.
    letras_digitadas = set()
    #usamos el abcedario para comparar letras.
    abcd = set(string.ascii_uppercase)
    while not (len(letras_adivinar) == 0 or cont == 7  or user_let == "0"):
        #En esta [list comprehension] tomamos cada letra en "palabra_aleatoria" si la letra esta en "letras_digitadas" muestra la letra sino
        #es remplazada por el signo '_'
        palabra_lista = [letra if letra in letras_digitadas else '_' for letra in palabra_aleatoria]
        #Se muestra en pantalla las letras que ya ha adivinado el jugador y las que no con el signo raya al piso.
        print(f"Palabra: {' '.join(palabra_lista)}")
        print("Digite una letra. En cualquier momento puede intentar adivinar la palabra completa. Para salir digite 0.")
        print("La palabra consta de",len(palabra_aleatoria),"letras.")
        print(f"Letras que has digitado:{' '.join(letras_digitadas)}")
        user_let = input(": ")
        user_let = user_let.upper()
        if user_let == "0":
            break
        #si lo que digito el usuario es mas de una letra se evalua si lo digitado es igual a lo que el juego tomo aleatoriamente.
        if len(user_let) > 1:
            if user_let == palabra_aleatoria:
                print("Adivinaste!!! el animal es:",user_let)
                user_let = "0"
                break
            #si lo que digito el jugador no es igual a la palabra que tomo el juego mostramos el text art dependiendo que numero contenga "cont".
            else:
                cont += 1
                fn_errors(cont)
                #Si la variable "cont" es igaul a 7 quiere decir que el jugador ya ha tenido siete errores por esa razon se rompe el ciclo
                #y se acaba el juego.
                if cont == 7:
                    break
        #Si el jugador escribio solo una letra se verifica que esta en el abcedario y si no esta en "letras_digitadas" se escribe esta letra
        #en "letras_digitadas".
        else:
            if user_let in abcd - letras_digitadas:
                letras_digitadas.add(user_let)
                #si la letra digitada por el usuario esta en "letras_adivinar" se retira del conjunto dicha letra.
                if user_let in letras_adivinar:
                    letras_adivinar.remove(user_let)
                else:
                    cont += 1
                    fn_errors(cont)
                    if cont == 7:
                        break
            #Se evalua si la letra digitada por el jugador esta en las letras que el anteriormente ya ha digitado.
            elif user_let in letras_digitadas:
                print("ya escogiste esa letra. Escoge otra")
    #Si en "letras_adivinar" existen objetos o "cont" es igual a siete o el usuario digito 0 significa que perdio.
    if len(letras_adivinar) != 0 or cont == 7 or user_let == "0":
        print("!Perdiste una pena!. La palabra es:",palabra_aleatoria)
    else:
        #Por el contrario si dentro de "letras_adivinar" no existen objetos o "cont" es diferente de siete o el usuario no digito 0.
        print("!!!Bien la palabra es",palabra_aleatoria,"Has Ganado!!!")


fn_juego_ahorcado()