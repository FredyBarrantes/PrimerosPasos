#Dos palabras ingresadas por el usuario verdadero si son anagramas falso si no lo son.
#Two word typed by user true if are anagrams false else.


#Usando el modulo "collections" importamos el objeto "Counter" // Using module "collections" import the object "Counter".
"""from collections import Counter


def fn_Anagrams():
    print("Digite dos palabras y la aplicacion le informara si son anagramas o si o lo son. Digite 0 para salir.")
    print("Typed two words and the app will show you if are anagrams or not. Type 0 to exit.")
    w1 = input("Primer palabra // First word: ")
    w2 = input("Segunda palabra // Second word: ")
    #"Counter" cuenta las veces que una letra esta dentro de la palabra, devuelve una diccionario donde la llave es la letra y el objeto
    #es la cantidad de veces que se encontro la letra, el diccionario esta ordenado de mayor a menor dependiendo del objeto.
    #"Counter" cont the times that found a letter inside de word, return a dictionary here the key is the letter and the object is
    #the amount of times that found the letter, the dictionary is sroted by largest to lower depending of the object.
    if Counter(w1) == Counter(w2):
        print("La palabra",w1,"y",w2,"son anagramas.")
    else:
        print("La palabra",w1,"y",w2,"No son anagramas.")"""



#Usando copias ordenadas de cadenas // Using sort strings

def fn_Anagrams():
    print("Digite dos palabras y la aplicacion le informara si son anagramas o si o lo son. Digite 0 para salir.")
    print("Typed two words and the app will show you if are anagrams or not. Type 0 to exit.")
    w1 = input("Primer palabra // First word: ").upper()
    w2 = input("Segunda palabra // Second word: ").upper()
    if sorted(w1) == sorted(w2):
        print("Las palabras",w1,"y",w2,"son anagramas.")
        print("The words",w1,"y",w2,"are anagrams.")
    else:
        print("Las palabras",w1,"y",w2,"No son anagramas.")
        print("The words",w1,"y",w2,"are Not anagrams.")


fn_Anagrams()