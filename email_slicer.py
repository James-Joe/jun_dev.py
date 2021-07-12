#In this project, I attempt to obtain the domain name of an email from user input.  I then take this
# information and send an email to the address that has been inputted.





def get_domain(email):
    name = email[0:email.index("@")]
    domain = email[email.index("@") + 1:]
    spliced_domain = domain.split(".")

    if spliced_domain[0] == "gmail":
      print("Well, " + name + " looks like you have a gmail account")
    elif spliced_domain[0] == "hotmail":
      print("Well, " + name + " looks like you have a hotmail account")
    else:
      print("Ohh!  Looks like you have a custom domain name ... Noice!")


print("Hey! What's your email?")
email = input()

get_domain(email)
