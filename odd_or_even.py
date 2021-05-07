#A simple program that asks the user for a number and tells the user if that number is odd or even.

intro = "Hello!  Give me a number, and I'll tell you if it is odd or even"

print(intro)

numb = int(input())

if numb % 2 == 0:
    print(str(numb) + " is an even number!")
else:
    print(str(numb) + " is an odd number")