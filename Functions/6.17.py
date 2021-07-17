def AREA(s1,s2,s3):
    s = (s1 + s2 + s3) / 2
    Area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
    print("AREA IS " , Area)


def isValid(s1,s2,s3):
    if (s1+s2 > s3) and ( s2+s3 > s1) and (s1+s3>s2):
        print("INPUT IS VALID AND " , end="")
        return True
    else:
        print("INPUT IS INVALID ACCORDING TO CONDITION OF QUESTION")

def main():
    s1,s2,s3 = eval(input("Enter 3 sides....."))
    if isValid(s1,s2,s3)==True:
        AREA(s1, s2, s3)
    else:
        print("INPUT IS INVALID ACCORDING TO CONDITION OF QUESTION")

main()