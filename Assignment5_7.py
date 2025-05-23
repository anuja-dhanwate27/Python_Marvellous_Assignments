def area(no1,no2):
    Result = no1 * no2
    return Result

def perimeter(no1,no2):
    Result = 2*(no1+no2)
    return Result


def main():
    print("Enter the length:")
    lenght = int(input())

    print("Enter widht")
    width = int(input())
    Ans = area(lenght,width)
    print("Area:",Ans)
    Ans = perimeter(lenght,width)
    print("Perimeter:",Ans)

if __name__ == "__main__":
    main()






    