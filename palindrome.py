#In this programme, I take an input of 5 words from the user, and check if any of those words are a palindrome.

def get_input():
    words = input("Please input 5 words or phrases separated by a comma\n")

    lst = words.split(",")

    return lst



def reverse_list(lst):

#    rev_lst = [i[::-1] for i in lst]
    for i in lst:
        if i != i[::-1]:
            continue
        print(i + " is a palindrome")
    



wrds = ["radar", "steve", "mum"]

for word in wrds:
    if word != word[::-1]:
        continue
    print(word + " is a palindrome")