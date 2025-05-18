def main():
    print("the size of the number")
    size = int(input())
    Data = list()
    print("Enter the number into list")
    for i in range(size):
        no = int(input())
        Data.append(no)

    max_element = Data[0]
    for i in Data:
        if i>max_element:
            max_element= i
            
    print("maximum Element is:",max_element)

if __name__=="__main__":
    main()






