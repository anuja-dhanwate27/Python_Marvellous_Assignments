def main():
    print("Enter the size of numbers")
    size = int(input())

    Data=list()
    print("Enter the numbers into list")
    for i in range(size):
        no = int(input())
        Data.append(no)
          

    sum = 0
    for i in Data:
        sum = sum + i
    print("Addition is:",sum)



if __name__=="__main__":
    main()

