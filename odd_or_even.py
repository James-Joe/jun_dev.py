# A simple program that asks the user for a number and tells the user if that number is odd or even.
# I created a function that takes the user's input, returns an answer and prompts them to try again.
# If they type 0, the program terminates.

intro = "Hello!  Give me a number, and I'll tell you if it is odd or even.  Type 0 to exit"

print(intro)




def odd_even():

    numb = int(input())

    if numb == 0:
        print("Bye for now")

    elif numb % 2 == 0:
        print(str(numb) + " is an even number.  Try again! Or type 0 to exit.")
        odd_even()

    else:
        print(str(numb) + " is an odd number.  Try again! Or type 0 to exit")
        odd_even()


odd_even()
        

