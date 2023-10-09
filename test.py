from random import randrange

game_over = False

# Level 1

print("Level 1")
level_1 = randrange(1, 10)

for try_level_1 in range(3):
    your_number = input('Choisissez un nombre entre 1 et 10 : ')
    your_number = int(your_number)
    
    if your_number == level_1:
        print("You win")
        break
    elif your_number > level_1:
        print("Too high")
    elif your_number < level_1:
        print("Too low")
else:
    print("You lose")
    game_over = True

# Level 2

if game_over == False :

    print("Level 2")
    
    level_2 = randrange(1, 20)

    for try_level_2 in range(5):
        your_number = input('Choisissez un nombre entre 1 et 20 : ')
        your_number = int(your_number)
        
        if your_number == level_2:
            print("You win")
            break
        elif your_number > level_2:
            print("Too high")
        elif your_number < level_2:
            print("Too low")
    else:
        print("You lose")
        game_over = True


# Level 3

if game_over == False :

    print("Level 3")

    level_3 = randrange(1, 30)

    for try_level_3 in range(7):
        your_number = input('Choisissez un nombre entre 1 et 30 : ')
        your_number = int(your_number)
        
        if your_number == level_3:
            print("You win")
            break
        elif your_number > level_3:
            print("Too high")
        elif your_number < level_3:
            print("Too low")
    else:
        print("You lose")
        game_over = True


if game_over == True:
    print("Game over")