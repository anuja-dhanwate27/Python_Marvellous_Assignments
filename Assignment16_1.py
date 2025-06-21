import sys

def main():
    fobj = open("student.txt","w")
    fobj.write("Anuja \n ")
    fobj.write("payal \n")
    fobj.write("Sakshi \n")
    fobj.write("Anushka \n")
    fobj.write("Siddhi \n")
    fobj.close()

if __name__ =="__main__":
    main()



    