import re

def phoneNumberValidator(number):
    
    pattern = '^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    if re.match(pattern, str(number)):
        #print("valid number")
        return True
    else:
        #print("Not valid number")
        return False

def emailValidator(email):
    pattern = '^[0-9a-z][0-9a-z_.]{4,18}@[0-9a-z]{3,8}.[a-z]{2,4}$'
    
    if re.match(pattern, str(email)):
        #print("valid number")
        return True
    else:
        #print("Not valid number")
        return False