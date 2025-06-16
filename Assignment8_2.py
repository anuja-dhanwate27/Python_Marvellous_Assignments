import threading

def Evenfactor(no):
    Evensum=0
    for i in range(1,no):
        if no%i==0 and i%2==0:
            Evensum=Evensum+i
    print("the even factor sum is:",Evensum)

def oddFactor(no):
    oddsum = 0
    for i in range(1,no):
        if no%i==0 and i%2!=0:
            oddsum=oddsum+i
    print("the oddfactor sum is:",oddsum)


def main():
    print("Enter number:")
    no1=int(input())

    T1=threading.Thread(target=Evenfactor,args=(no1,))
    T1.start()
    T1.join()
    T2=threading.Thread(target=oddFactor,args=(no1,))
    T2.start()
    T2.join()

    print("Exit for main")

if __name__ =="__main__":
    main()

