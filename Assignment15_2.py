import os

def main():
    print("Enter the file name")
    FileName = input()

    fobj = open(FileName,"r")
    data = fobj.read()
    print("Data from the file : ",data)
    fobj.close()


if __name__ == "__main__":
    main()

    