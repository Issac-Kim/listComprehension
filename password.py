#First

def passCheck(password):
    password = list(password)
    if len([x for x in password if x.islower()]) == 0:
        return False
    if len([x for x in password if x.isupper()]) == 0:
        return False
    if len([x for x in password if x.isdigit()]) == 0:
        return False
    else:
        return True

#Second

def passIntegrity(password):
