#A simple program that asks the user for a number and tells the user if that number is odd or even.
#I hope to build on this program so that it can keep asking the user to enter a number until they choose to exit the program.

intro = "Hello!  Give me a number, and I'll tell you if it is odd or even.  Type 0 to exit"

print(intro)




def odd_even():

    numb = int(input())

    if numb == 0:
        print("Bye for now")

    elif numb % 2 == 0:
        print(str(numb) + " is an even number.  Try again!")
        odd_even()

    else:
        print(str(numb) + " is an odd number.  Try again!")
        odd_even()


odd_even()
        

