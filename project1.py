name = input("Hi type your name : ")
print(f"Hello {name} welcome to my game!")

should_play = input("Do you want to play the game?").lower()

if should_play == "y" or "yes":
    print("We are gonna play!")

    direction = input("Which direction you want to go (left/right) : ").lower()

    if direction == "right":
        print("Game Over you crushed by rock!")
    elif direction == "left":
        movement = input("Do you want to drink water or not : ").lower()

        if movement == 'yes' or 'y':
            print("Congrats!! you won the game")
        elif movement == "no" or 'n':
            print("GAME OVER!! You die by dehydration")
        else:
            print("Invalid Output, GAME OVER")
        
else:
    print("We are not playing then!!")

    