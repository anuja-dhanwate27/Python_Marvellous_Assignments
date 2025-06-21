def main():
    print("Enter the  first file name")
    FileName1 = input()
    fobj1 = open(FileName1,"r")
    print("Enter the second file name")
    FileName2 = input()
    
    fobj2 = open(FileName2,"x")
    for line in fobj1:
        if line.strip()!="":
            fobj2.write(line)

    fobj1.close()
    fobj2.close()

if __name__=="__main__":
    main()



            
