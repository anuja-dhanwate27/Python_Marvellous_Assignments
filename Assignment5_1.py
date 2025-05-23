def Addition(no1,no2):
    Result = no1 + no2
    return Result

def Diffrence(no1,no2):
    Result = no1 - no2
    return Result


def Product(no1,no2):
    Result = no1 * no2
    return Result

def Division(no1,no2):
    Result = no1/no2
    return Result

def main():
    print("Enter the first number")
    value1 = int(input())
    print("Enter the second number")
    value2 = int(input())

    Ans = Addition(value1,value2)
    print("Sum:",Ans)

    Ans = Diffrence(value1,value2)
    print("Difference:",Ans)

    Ans = Product(value1,value2)
    print("Product:",Ans)

    Ans =Division(value1,value2)
    print("Division:",Ans)


if __name__ =="__main__":
    main()


