import string 
import random


# Generating name functions 
# You can create different surnames to increase the variety of usernames.
def generatingName():
    firstName = ["Divya", "Payal" ]

    surName = ["Rajawat", "Chauhan"]
    return ''.join(random.choice(firstName) + ' '  + random.choice(surName))    


# Generating a username
def username(size = 6, chars  = string.ascii_lowercase + random.choice(['.', '_'])):
    return ''.join(random.choice(chars) for _ in range(size))


# Generating a Email
def generatingEmail() :
    return ''.join(username() + '@mailr24.com')

