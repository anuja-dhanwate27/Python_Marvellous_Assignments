import os

def main():
    print("Enter the file name ")
    FileName = input()
    ret = os.path.exists(FileName)
    if(ret==True):
        print("File is exists in current directory")
    else:
        print("There is no such a file in current directory")

if __name__ =="__main__":
    main()

    


    