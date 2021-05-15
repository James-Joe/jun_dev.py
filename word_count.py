#This program takes a text input and returns the word_count

some_input = "haec uestis priscis hominum uariata figuris"
 
make_list = some_input.split()

length_lst= len(make_list)

print("Your input has " + str(length_lst) + " words")