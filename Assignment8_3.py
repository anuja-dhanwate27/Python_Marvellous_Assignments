import threading

def EvenList(data):
    sum = 0
    for i in data:
        if i%2==0:
            sum=sum+i
    print("the even element sum is:",sum)

def OddList(data):
    sum = 0
    for i in data:
        if i%2!=0:
            sum=sum+i
    print("The odd element sum are:",sum)

def main():

    Data=list()
    print("Enter the size of list")
    size = int(input())
    print("Enter element into list:")
    for i in range(size):
        no=int(input())
        Data.append(no)

    T1=threading.Thread(target=EvenList,args=(Data,))
    T2=threading.Thread(target=OddList,args=(Data,))
    T1.start()
    T2.start()

if __name__=="__main__":
    main()




















