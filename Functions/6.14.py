def pi():
    for i in range(1 , 902 , 100):
            m = 0
            for j in range(1,i+1):
                m = m + ((-1) ** (j + 1)) / (2*j - 1)
            print(format(i , "3d" ) , "   " , format(m * 4 , "5.3f" ) )

def main():
    pi()

main()