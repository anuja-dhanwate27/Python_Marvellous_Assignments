def main():
    print("enter the number")
    num = int(input())
    if num >1:
        for i in range(2,num):
            if (num %i)==0:
                print("it is not a prime number")
                break
                
        else:
            print("it is a prime number")
        
if __name__=="__main__":
    main()
