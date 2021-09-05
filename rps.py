#This programme allows two users to input rock, paper, or scissors in order to play the game.

from getpass import getpass
import random



def user_input_one():

    input_one = getpass(prompt="Player one, \nplease choose rock, paper, or scissors\n")
    input_one = input_one.lower()

    if input_one == "rock" or input_one == "paper" or input_one == "scissors":
        return input_one 
        
    else:
        print("Please choose a valid option")
        return user_input_one()
        



def user_input_two():

    input_two = getpass(prompt="Player two, \nplease choose rock, paper, or scissors\n")
    input_two = input_two.lower()

    if input_two == "rock" or input_two == "paper" or input_two == "scissors":
        return input_two
    
    else:
        print("Please choose a valid option")
        return user_input_two()



def computer_input():

    choices = ["rock", "paper", "scissors"]

    rand_num = random.randrange(0, 3)

    choice = choices[rand_num]

    return choice




def decide_winner(input_one, input_two):

    print("================\n\n\nPlayer one chose " + str(input_one)
    + "\nPlayer two chose " + str(input_two) + ".\n\n\n================")


    if input_one == input_two:
        print("It's a draw!")

    elif (input_one == "rock" and input_two == "scissors") or (input_two == "rock" and input_one == "scissors"):
        print("Rock beats scisors")

    elif (input_one == "scissors" and input_two == "paper") or (input_two == "scissors" and input_one == "paper"):
      print("Scissors beats paper")
    
    elif (input_one == "paper" and input_two == "rock") or (input_two == "paper" and input_one == "rock"):
      print("Paper beats rock")


def restart():

    replay = input("++++++++++++\n\nWould you like to play again?\n\n(y/n)\n\n++++++++++++\n\n")

    replay = replay.lower()

    if replay == "y":
        return main()
    elif replay == "n":
        print("\n\nThanks for playing!\n\n")
        raise SystemExit
    else:
        print("Please provide a valid input (y/n).\n")
        return restart()

def main():

    input_one = user_input_one()
    input_two = user_input_two()
    decide_winner(input_one, input_two)
    restart()
    

main()
