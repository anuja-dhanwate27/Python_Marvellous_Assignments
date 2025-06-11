from functools import reduce 

def chkprime(num):
    if num >1:
        for i in range(2,num):
            if (num%i==0):
                return False
        else:
            return True

def multi(num):
    return num*2

def maximum(x,y):
    if x>y:
        return x
    else:
        return y
    

print("Enter the size of list")
size = int(input())

Data =list()
print("Enter the element")
for i in range(size):
    no = int(input())
    Data.append(no)

FData = list(filter(chkprime,Data))
print("Filter data is:",FData)

MData = list(map(multi,FData))
print("Map data is:",MData)

RData= reduce(maximum,MData)
print("Reduce data is:",RData)


