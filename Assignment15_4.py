import sys

def main():

    
    FirstFileName = sys.argv[1]
    fobj = open(FirstFileName,"r")
    Fdata = fobj.read()
    
    
    SecondFileName = sys.argv[2]
    fobj = open(SecondFileName,"r")
    Sdata = fobj.read()

    if (Fdata == Sdata):
         print("success")
    else:
         print("Failure")

if __name__ =="__main__":
    main()
