def chkEven(no):
    if (no%2==0):
        print(no,"Is an odd num")
    else:
        print(no,"Is an odd number")

def main():
    print("Enter the number")
    num = int(input())
    chkEven(num)

if __name__ == "__main__":
    main()


