import sys

def main():
    

    FileName = sys.argv[1]

    fobj = open(FileName,"r")
    data = fobj.read()

    fobj = open("Demo.txt","w")
    newData = fobj.write(data)

    print("data copied in to Demo.txt succesfully")


if __name__=="__main__":
    main()




