email = "jacobassplayer@hotmail.co.uk"

#get_username = email.split("@")

#username = get_username[0]

name = ""

for i in email:
    if i == "@":
        break
    name += i


print(name)


