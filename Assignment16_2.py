def main():
    fobj =open("data.txt","r")
    data = fobj.read()
    print("Data from the file is:",data)
    fobj.close()

if __name__ =="__main__":
    main()

    