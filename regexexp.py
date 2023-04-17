import re

email = input("Whats your email?").strip()
if re.search(r"^.+@.+\.com$", email):
    print("Valid")
#if re.search("@", email):
    #print("Valid")

#username, domain = email.split("@")

#if username and domain.endswith(".com"):
    #print("Valid")
else:
    print("Invalid")
