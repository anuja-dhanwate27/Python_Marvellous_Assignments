def main():
    print("The size of the element ")
    size = int(input())

    Data = list()
    print("enter the element into list")
    for i in range(size):
        no = int(input())
        Data.append(no)

    min_element= Data[0]
    for i in Data:
        if i < min_element:
            min_element = i
    print("The minimun ",min_element)

if __name__=="__main__":
    main()


