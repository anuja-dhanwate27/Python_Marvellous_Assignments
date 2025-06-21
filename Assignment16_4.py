def main():

    fobj = open("number.txt","w")
    count = 0
    while count <10:
        num = input()
        fobj.write(num +"\n")
        count = count + 1

    fobj.close()

if __name__ =="__main__":
    main()



