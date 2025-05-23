def checkprime():
    print("Enter the number")
    no = int(input())
    if no>1:
        for i in range(2,no):
            if no%i==0:
                print(no,"is not  prime number ")
                break
        else:
             print(no,"is prime number")

if __name__ =="__main__":
    checkprime()