email = "jacobassplayer@hotmail.co.uk"


# Method 1

# get_username = email.split("@")

# username = get_username[0]



# Method 2

# name = ""

# for i in email:
  #  if i == "@":
   #     break
   # name += i

# print(name)

# Method 3

def method_3(email):
    name = email[0:email.index("@")]
    print(name)

method_3(email)
