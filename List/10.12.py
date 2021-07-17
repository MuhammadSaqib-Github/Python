def gcd(numbers):
    x=numbers[0]
    for i in range(1,len(numbers)):
        while True:  
          if x>numbers[i]:
            if x%numbers[i]==0:
                x = numbers[i]
                break
            x = x - numbers[i]
          else:
            if numbers[i]%x==0:
                x  = x
                break
            numbers[i] =  numbers[i] - x
            
    return x
        
def main():
    lst=input("enter no.s sep bys commas")
    lst = lst.split()
    numbers = [int(x) for x in lst]
    g= gcd(numbers)
    print("GCD IS " , g)

main()