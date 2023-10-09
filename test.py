from random import randrange
import threading

count_level = 1
your_number = 0
count_round = 0

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
    def continue_or_quit(count_level):
        input_user = input("LEVEL X, Il vous reste X solde,Voulez-vous continuer ? (y/n) : ")
        if input_user == "n":
            print("Game Over")
            exit()

    # Level 1

    print("Round", count_round)

    if count_level == 1:

        if count_round > 0:
            continue_or_quit(count_level)

        print("Level 1")
        level_1 = randrange(1, 10)
        print(level_1)

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
                break
            elif your_number > level_1:
                print("Too high")
            elif your_number < level_1:
                print("Too low")
        else:
            print("You lose")
            count_level -= 1

    # Level 2

    if count_level == 2:

        continue_or_quit(count_level)

        print("Level 2")
        level_2 = randrange(1, 20)
        print(level_2)

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
                break
            elif your_number > level_2:
                print("Too high")
            elif your_number < level_2:
                print("Too low")
        else:
            print("You lose")
            count_level -= 1

    # Level 3

    if count_level == 3:

        continue_or_quit(count_level)

        print("Level 3")
        level_3 = randrange(1, 30)
        print(level_3)

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
