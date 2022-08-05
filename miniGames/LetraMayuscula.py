#Dada una cadena: el nombre de una persona, con nombre y apellido.Debe verificar si la primera letra del nombre y el apellido están
#en mayúscula.
#Este tipo de casing donde la primera letra de cada palabra está en mayúscula se llama titulo del caso.Así que tienes que comprobar
#si el nombre está en mayúsculas y minúsculas:  1. En caso afirmativo, envíe un mensaje de que el formato está en mayúsculas y 
#minúsculas.    2. De lo contrario, devuelva una copia de la cadena formateada en el caso del título.

#Strings: name of a person, with name and lastname. Verify if the first letter of name and the last name are in uppercase.


def fn_title():
    name = 0
    while name != "0":
        name = input("Digite nombre y apellido\n: ")
        if name == "0":
            break
        if name.istitle():
            print("El nombre y el apellido inician con mayuscula.")
            print("Name and lastname start with capital letter.")
        else:
            name = name.title()
            print("Se ha modificado el nombre y el apellido para que inicien con letra mayuscula.",name)
            print("It's modified the name and lastname to start with capital letter.",name)


fn_title()