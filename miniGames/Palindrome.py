#Verificar si una cadena dada es o no un palíndromo.
#verify if a string typed is or not a palindrome.


def fn_palindrome():
    word_usr = 1
    while word_usr != "0":
        print("Digite una palabra y el programa le informara si es palindroma, para salir digite 0")
        print("Type a word and the program will show you if it's palindrome, to exit type 0")
        word_usr = input(": ")
        if word_usr == "0":
            break
        #palindrome = word_usr[::-1]    #a path how is posible reverse the word.
        palindrome = ''.join(reversed(word_usr))    #other way to reverse a word.
        if word_usr == palindrome:
            print("La palabra",word_usr,"es palindroma.")
            print("Word",word_usr,"is palindrome.")
        else:
            print("La palabra",word_usr,"No es palindroma")
            print("La palabra",word_usr,"No es palindroma")


fn_palindrome()