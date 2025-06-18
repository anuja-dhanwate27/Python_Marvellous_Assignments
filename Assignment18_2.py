import os 
def main():
    print("Enter the file name ")
    FileName = input()
    fobj=open(FileName,"r")
    data = fobj.read()
    print("File data is:",data)

if __name__ =="__main__":
    main()

    

