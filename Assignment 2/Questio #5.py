small=0
cap=0
dig=0
sym =0
def smallLetter(val):
    global small
    if val<=97 and val>=122:
        small=+1

def capitalLetter(val):
    if val<=65 and val>=90:
        return True
        cap+=1

def Digit(val):
    global dig
    if val<=48 and val>=57:
        dig+=1

def Symbol(val):
    global sym
    if (val<=32 and val>=47) or (val<=58 and val>=64) or (val<=91 and val>=96) or (val<=123 and val>=126):
        sym+=1
def main():
    password = input("Password must fullfil the following conditions \n \
     • At least 1 letter between [a-z] and 1 letter between [A-Z].\n \
     • At least 1 number between [0-9]. \n \
     • At least 1 character from [$#@]. \n \
     • Minimum length 6 characters. \n \
     • Maximum length 16 characters. \n Enter Password: ")

    if len(password)>=6 and len(password)<=16:
        for ch in password:
            val = ord(ch)
            smallLetter(val)
            capitalLetter(val)
            Digit(val)
        if small != 0 and cap != 0 and dig != 0 and sym != 0:
            print("Password meets with required criteria")
        else:
            print("Password does'nt meet with required criteria")
    else:
        print("Password must contain atleast 6 and atmost 16 characters")
main()