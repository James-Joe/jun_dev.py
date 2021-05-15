#Madlibs - just scribbles for now.  Need to think how best to get the input
# and display it

print("Welcome to Mad libs!")



#This function provides the basic functionallity of the game.
#The function finishes by calling play_again(), which gives the player
#the choice to try again or quit the program.

def mad_lib():
    part_1 = "I went to the store and saw a "
    print(part_1)
    entry_1 = input()
    part_2 = "I went in and ask the assistant where did he find the " + entry_1 + " and he said "
    print(part_2)
    entry_2 = input()
    print(part_1 + entry_1 + part_2 + entry_2)
    play_again()

def play_again():    
    print("Thanks for playing. Do you want to play again? [Y/N]")
    entry_3 = input()
    if entry_3 == "Y" or entry_3 == "y":
        mad_lib()
    elif entry_3 == "N" or entry_3 == "n":
        print("Okay! see you later!")
    else:
        print("Sorry that isn't a valid input.")
        play_again()




mad_lib()


