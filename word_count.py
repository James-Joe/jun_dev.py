#This program takes a text input and returns the word_count.
# 
# word_count takes a filename as input, opens it, reads it, then turns the input
# into a list (make_list) separated by whitespace using .split().
# A new_list is then created that takes out any punctuation that may be counted 
# as a word - such as an elipsis ("...").  

# prompt_continue() then asks the user if they want to count something 
# else or to quit the program.




def word_count():
    print("Provide the file name of the text you would like us to word count")
    some_input = open(input())
    
    make_list = some_input.read().split()

    new_list = [word for word in make_list if word.startswith((".", ",", ";", ":", "?", "!", "-")) == False]

    length_lst= len(new_list)

    print("Your text has " + str(length_lst) + " words.")

    prompt_continue()

    
def prompt_continue():

    print("Would you like us to read another text? [Y/N]")
    restart = input()

    if restart == "Y" or restart == "y":
        word_count()
    elif restart == "N" or restart == "n":
        print("Goodbye!")
    else:
        print("Please enter a valid input [Y/N]")
        prompt_continue()



word_count()
