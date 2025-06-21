def main():
    print("Enter the file name:")
    FileName = input()
    fobj = open(FileName,"r")
    lines = fobj.readlines()
    for i in lines:
        words = i.split()
        if len(words)>5:
            print(i)

    

if __name__=="__main__":
    main()

