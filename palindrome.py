#In this programme, I take an input of 5 words from the user, and check if any of those words are a palindrome.

def is_palindrome():
    words = input("Please input 5 words or phrases separated by a comma\n")

    lst = words.lower().split(", ")
    #print(lst)

    for i in lst:
        if i != i[::-1]:
            continue
        print(i + " is a palindrome")
    


is_palindrome()