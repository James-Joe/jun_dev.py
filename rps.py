#This programme allows two users to input rock, paper, or scissors in order to play the game.

def user_input_one():
    input_one = input("Player one, \nplease choose rock, paper, or scissors\n")

    if input_one != "rock" or input_one != "paper" or input_one != "scissors":
        print("Please choose a valid option")
        user_input_one()
    else:
        return input_one.lower()  

def user_input_two():
    input_two = input("Player two, \nplease choose rock, paper, or scissors\n")

    if input_two != "rock" or input_two != "paper" or input_two != "scissors":
        print("Please choose a valid option")
        user_input_two()
    else:
        return input_two.lower() 



def decide_winner(input_one, input_two):

    if input_one == input_two:
        print("It's a draw")
        
    elif:
