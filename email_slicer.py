#In this project, I attempt to obtain the domain name of an email from user input.  I then take this
# information and send an email to the address that has been inputted.


import smtplib, ssl, getpass 

def send_email(recipient):
  port = 587  # For starttls
  smtp_server = "smtp.gmail.com"
  sender_email = "test.py.67@gmail.com"
  receiver_email = recipient
  password = getpass.getpass()
  message = """\
  Subject: Hi there

  This message is sent from Python."""

  context = ssl.create_default_context()
  with smtplib.SMTP(smtp_server, port) as server:
      server.ehlo()  # Can be omitted
      server.starttls(context=context)
      server.ehlo()  # Can be omitted
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)

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
    send_email(email)


print("Hey! What's your email?")
email = input()

get_domain(email)
