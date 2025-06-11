def main():
    print("Enter the file name")
    FileName = input()
    print("Enter the string")
    string = input()

    fobj = open(FileName,"r")
    data = fobj.read()

    count = data.count(string)

    print(count)
if __name__ =="__main__":
    main()
    