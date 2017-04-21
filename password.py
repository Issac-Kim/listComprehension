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
    password = list(password)
    if(passCheck(password)):
        score = 1
        if len(password) == 3:
            return 1
        alpha = (len([x for x in password if x.isalpha()]) - 1) / 2
        num = len([x for x in password if x.isdigit()])
        spec = len([x for x in password if not x.isalnum()])
        if alpha > 3:
            alpha = 3
        if num > 3:
            num = 3
        if spec > 3:
            spec = 3
        return score + alpha + num + spec
    else:
        return 0


