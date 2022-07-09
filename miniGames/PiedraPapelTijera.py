#Piedra, papel o tijera contra la pc.
#stone, paper or scissors against pc.

import random

def piedra_papel_tijera():
    vec = ["piedra/stone", "papel/paper", "tijera/scissors"]    #It's created a list with the words.
    score_comp = 0
    score_player = 0
    while not (score_comp == 2 or score_player == 2):   #while score_comp or score_player are different of 2, run that is inside the "while".
        num_usr = 10    #num_usr this variable is initiated with the number 10 because forwards it's necesary that be differen of 0,1,2,3
        ran_num = random.randint(0, 2)  #ran_num take a random number among 0 and 2.
        try:
            while not (num_usr == 0 or num_usr == 1 or num_usr == 2 or num_usr == 3):   #if the player choose 0,1,2,3 this "while" jump and continue. Always when the cycle is repeted the variable num_usr start with the number 10 to obligate the app to execute this "while".
                print("////-////-////-////-////-////")
                print("//// Digite 0 = Piedra.  ////\n//// Digite 1 = Papel.  ////\n//// Digite 2 = Tijera. ////\n//// Digite 3 = Salir. ////")
                print("//// Type 0 = Stone.  ////\n//// Type 1 = Paper.  ////\n//// Type 2 = Scissors. ////\n//// Type 3 = Exit. ////")
                print("////-////-////-////-////-//")
                num_usr = int(input(": "))
                if num_usr == 3:
                    raise ZeroDivisionError

        except ValueError:
            print("Digite 0, 1, 2 or 3\nType 0, 1, 2 or 3 ")
        except ZeroDivisionError:
            break

        else:
            obj_comp = vec[ran_num]
            obj_usr = vec[num_usr]
            print("Has escogido",obj_usr,"\nYou've chosen",obj_usr)
            if obj_comp == obj_usr:
                print("La pc tambien saco",obj_comp,". Sin puntos.")
                print("The pc as well took",obj_comp,". No points")

            if obj_comp == "piedra" and obj_usr == "tijera":
                score_comp += 1
                print("La pc escogio",obj_comp,". Te gana un punto.")
                print("The pc taked",obj_comp,". It win one point")
            elif obj_comp == "tijera" and obj_usr == "piedra":
                score_player += 1
                print("La pc escogio",obj_comp,". Le ganas un punto.")
                print("The pc took",obj_comp,". You win one point")
            
            if obj_comp == "papel" and obj_usr == "piedra":
                score_comp += 1
                print("La pc escogio",obj_comp,". Te gana un punto.")
                print("The pc taked",obj_comp,". It win one point")
            elif obj_comp == "piedra" and obj_usr == "papel":
                score_player += 1
                print("La pc escogio",obj_comp,". Le ganas un punto.")
                print("The pc took",obj_comp,". You win one point")

            if obj_comp == "tijera" and obj_usr == "papel":
                score_comp += 1
                print("La pc escogio",obj_comp,". Te gana un punto.")
                print("The pc taked",obj_comp,". It win one point")
            elif obj_comp == "papel" and obj_usr == "tijera":
                score_player += 1
                print("La pc escogio",obj_comp,". Le ganas un punto.")
                print("The pc took",obj_comp,". You win one point")

            print("Puntos jugador:",score_player,"\nScore player:",score_player)
            print("Puntos Pc:",score_comp,"\nScore Pc:",score_comp)

    if score_comp == 2:
        print("Te ha ganado la computadora.\nThe computer won.")
    elif score_player == 2:
        print("Le ganaste a la computadora.\nYou win.")


piedra_papel_tijera()