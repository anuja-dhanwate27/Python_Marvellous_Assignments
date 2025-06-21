def main():

    fobj = open("Source.txt","r")
    data = fobj.read()
    fobj = open("destination.txt","w")
    fobj.write(data)

    fobj.close()


if __name__ =="__main__":
    main()
    
    