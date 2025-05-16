import Arithmatic
def main():
    print("Enter the  first number")
    value1 =int(input())
    print("enter the second number")
    value2 = int(input())
    Ans1 = Arithmatic.Add(value1,value2)
    print("Addition is ",Ans1)
    Ans2 = Arithmatic.Sub(value1,value2)
    print("substraction is",Ans2)
    Ans3 = Arithmatic.mult(value1,value2)
    print("multiplication is:",Ans3)
    Ans4 = Arithmatic.div(value1,value2)
    print("dividon is:",Ans4)


if __name__ =="__main__":
    main()

    