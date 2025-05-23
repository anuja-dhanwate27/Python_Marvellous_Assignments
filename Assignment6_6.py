def main():
    print("enter the number")
    no = int(input())
    for i in range(1,no+1):
        for j in range(i,no+1):
           print("* "*j)
           break
       
    

if __name__=="__main__":
    main()


