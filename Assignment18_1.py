import os

def main():

    print("Enter the file name")
    FileName = input()
    Result = os.path.exists(FileName)
    if(Result==True):
        print("File is exit in current directory")
    else:
        print("File is not exists in current directory")
if __name__=="__main__":
    main()

    


