from functools import reduce
def chknum(no):
    return no%2==0

def square(no):
    return no**2

def sum(no1,no2):
    return no1+no2

print("Enter the size of list:")
size = int(input())
data = list()
print("Enter the values:")
for i in range(size):
    no=int(input())
    data.append(no)

Fdata = list(filter(chknum,data))
print("filter data is",Fdata)

Mdata=list(map(square,Fdata))
print("map data is:",Mdata)

Rdata=reduce(sum,Mdata,)
print("Reduce data is:",Rdata)

