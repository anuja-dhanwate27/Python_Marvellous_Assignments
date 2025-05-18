def main():
    print("Enter the size number")
    size =int(input())
    Data=list()
    print("Enter the element into list")
    for i in range(size):
        no = int(input())
        Data.append(no)


    print("Enter element to search its frequency:")
    N = int(input())
    count = 0
    for i in Data:
        if i == N:
            count = count+1
    print("The frequency of number is:",count)

main()

