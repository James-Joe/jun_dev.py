#This program takes a text input and returns the word_count

some_input = open("eliot.txt")
 
make_list = some_input.read().split()

new_list = [word for word in make_list if word.startswith((".", ",", ";", ":", "?", "!")) == False]

print(new_list)

length_lst= len(new_list)

print("Your input has " + str(length_lst) + " words")