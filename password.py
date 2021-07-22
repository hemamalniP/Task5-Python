import re
inp= input("Enter password")
x = True
while x:  
    if (len(inp)<6 or len(inp)>12):
        break
    elif not re.search("[a-z]",inp):
        break
    elif not re.search("[0-9]",inp):
        break
    elif not re.search("[A-Z]",inp):
        break
    elif not re.search("[$#@]",inp):
        break
    elif re.search("\s",inp):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Invalid Password")
    
