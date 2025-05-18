import MarvellousNum

def ListPrime():
    print("The size of element")
    size = int(input())

    Data =list()
    print("Enter the elemet into list")
    for i in range(size):
        no = int(input())
        Data.append(no)


    Ans = MarvellousNum.checkprime(num)
    sum = 0
    for num in Data:
        if MarvellousNum.checkprime(num):
            sum = sum+sum
        print("The sum is:",sum)

if __name__=="__main__":
    ListPrime()


        






