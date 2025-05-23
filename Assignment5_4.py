def largeNum(X,Y,Z):
    if(X>Y):
        print("Largest number is:",X)
    elif(Y>X):
        print("largest number is:",Y)
    else:
        print("largest number is:",Z)

def main():
    print("Enter the numbers:")
    no1 = int(input())
    no2 = int(input())
    no3 = int (input())
    

    largeNum(no1,no2,no3)

if __name__ == "__main__":
    main()

    