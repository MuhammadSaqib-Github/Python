p1,p2,p3 = 0,0,0
occurence = 0
def check(ch):
    
    global  p1,p2,p3,occurence
    occurence1 , occurence2 ,occurence3 = 0,0,0
    ascii = ord(ch)
    if ascii==91 or ascii==93:
        p1 = p1 + 1
        occurence1 = occurence1 + 1
        
    if ascii==123 or ascii==125:
        p2 = p2 + 1
        occurence2 = occurence2 + 1
        
    if ascii==41 or ascii==40:
        p3 = p3 + 1
        occurence3 = occurence3 + 1
    
    if occurence1%2==0:
        occurence = occurence + occurence1
        
    
    if occurence2%2==0:
        occurence = occurence + occurence2
        
    
    if occurence3%2==0:
        occurence = occurence + occurence3
        
           
def main():
    global  p1,p2,p3,occurence
    string = input("Enter a string containging")
    for c in string:
        check(c)
    if occurence%2==0:
            print("Complete pair")
    else:
            print("not completed pair")
main()