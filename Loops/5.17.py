'''
(Display the ASCII character table) Write a program that displays the characters
in the ASCII character table from ! to ~. Display ten characters per line.
The characters are separated by exactly one space
'''

n=1
i = 33
while i <= 126:
    ch = chr(i)
    if n%11==0:
        print(chr(i) , " " ,  ord(ch) )
    else:
        print(chr(i), " " , ord(ch)  , end=" " )
    i+=1
    n+=1
