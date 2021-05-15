#This program takes a text input and returns the word_count

some_input = open("eliot.txt")
 
make_list = some_input.read().split()

#the loop below doesn't do what I want to yet - but my results are just as good as libreoffice at the moment

for word in make_list:
    for character in word:
        if character.isalnum() == False:
            word.replace(character, " ")

print(make_list)

length_lst= len(make_list)

print("Your input has " + str(length_lst) + " words")