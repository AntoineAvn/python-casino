from random import randrange
import threading
from statsClass import Stats, readData

count_level = 1
your_number = 0
count_round = 0
solde = 0
mise = 5

while True:

    def input_with_timeout(prompt, timeout):
        print(prompt)
        timer = threading.Timer(timeout, lambda: print("\nGame Over") or exit())
        try:
            timer.start()
            return int(input())
        finally:
            timer.cancel()

    # Choix à l'utilisateur de continuer ou arrêter le jeu
    def continue_or_quit(count_level, solde):
        input_user = input("Vous êtes au level " + str(count_level) + ", Il vous reste " + str(solde) + " euro, Voulez-vous continuer ? (y/n) : ")
        if input_user == "n":
            print("Game Over")
            exit()

    # Choix à l'utilisateur de rentrer un solde au début du jeu
    if count_round == 0:
        try:
            while True :
                print("Round", count_round)

                solde = int(input("Choisissez un solde entre 1 et 100 : "))
                if solde >= 1 and solde < 100:
                    break
        except ValueError:
            print("Entrée invalide, ce n'est pas un nombre.")
            continue


    # Level 1 (gagne la mise)

    if count_level == 1:

        if count_round > 0:
            continue_or_quit(count_level, solde)

        print("Level 1")
        level_1 = randrange(1, 10)
        print(level_1)

        solde -= mise
        print('solde : ', solde)

        for try_level_1 in range(3):
            try:
                while True :
                    your_number = input_with_timeout('Choisissez un nombre entre 1 et 10 : ', 10)
                    if your_number >= 1 and your_number < 10:
                        break

            except ValueError:
                print("Entrée invalide, ce n'est pas un nombre.")
                continue
            
            if your_number == level_1:
                print("You win")
                count_round += 1
                count_level += 1
                solde += 5
                break
            elif your_number > level_1:
                print("Too high")
            elif your_number < level_1:
                print("Too low")
        else:
            print("You lose")
            count_level -= 1

    # Level 2 (gagne la mise * 2)

    if count_level == 2:

        continue_or_quit(count_level, solde)

        print("Level 2")
        level_2 = randrange(1, 20)
        print(level_2)

        solde -= mise
        print('solde : ', solde)

        for try_level_2 in range(5):
            try:
                while True :
                    your_number = input_with_timeout('Choisissez un nombre entre 1 et 20 : ', 10)
                    if your_number >= 1 and your_number < 20:
                        break
            except ValueError:
                print("Entrée invalide, ce n'est pas un nombre.")
                continue
            
            if your_number == level_2:
                print("You win")
                count_round += 1
                count_level += 1
                solde += mise * 2
                break
            elif your_number > level_2:
                print("Too high")
            elif your_number < level_2:
                print("Too low")
        else:
            print("You lose")
            count_level -= 1

    # Level 3 (gagne la mise * 4)

    if count_level == 3:

        continue_or_quit(count_level, solde)

        print("Level 3")
        level_3 = randrange(1, 30)
        print(level_3)

        solde -= mise
        print('solde : ', solde)

        for try_level_3 in range(7):
            try:
                while True :
                    your_number = input_with_timeout('Choisissez un nombre entre 1 et 30 : ', 10)
                    if your_number >= 1 and your_number < 30:
                        break
            except ValueError:
                print("Entrée invalide, ce n'est pas un nombre.")
                continue
            
            if your_number == level_3:
                print("You win")
                count_round += 1
                count_level += 1
                solde += mise * 4
                print('Bravo vous avez gagné ! Votre solde final est de : ' + str(solde))
                break
            elif your_number > level_3:
                print("Too high")
            elif your_number < level_3:
                print("Too low")
        else:
            print("You lose")
            count_level -= 1

    # Game over
    if count_level == 0:
        print("Game Over")
        break
