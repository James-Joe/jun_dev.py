#This programme allows two users to input rock, paper, or scissors in order to play the game.

def user_input_one():
    input_one = input("Player one, \nplease choose rock, paper, or scissors\n")
    input_one.lower()

    if input_one == "rock" or input_one == "paper" or input_one == "scissors":
        return input_one 
        
    else:
        print("Please choose a valid option")
        return user_input_one()

def user_input_two():
    input_two = input("Player two, \nplease choose rock, paper, or scissors\n")
    input_two.lower()

    if input_two == "rock" or input_two == "paper" or input_two == "scissors":
        return input_two
    
    else:
        print("Please choose a valid option")
        return user_input_two()



def decide_winner(input_one, input_two):

    print("================\n\n\nPlayer one choose " + str(input_one)
    + "\nPlayer two choose " + str(input_two) + ".\n\n\n================")


    if input_one == input_two:
        print("It's a draw!")

    elif (input_one == "rock" and input_two == "scissors") or (input_two == "rock" and input_one == "scissors"):
        print("Rock beats scisors")

    elif (input_one == "scissors" and input_two == "paper") or (input_two == "scissors" and input_one == "paper"):
      print("Scissors beats paper")
    
    elif (input_one == "paper" and input_two == "rock") or (input_two == "paper" and input_one == "rock"):
      print("Paper beats rock")


def main():
    input_one = user_input_one()
    input_two = user_input_two()
    decide_winner(input_one, input_two)

main()




    
