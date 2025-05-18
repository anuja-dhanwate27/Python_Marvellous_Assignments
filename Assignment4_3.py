from functools import reduce

def checkNum(No)
    return No>=70 and No<=90
    
def Increase(No):   
    return No+10

def product(No1,No2):
    return No1*No2
     
print("Enter the size of list:")
size = int(input())
data = list()
print("Enter the values:")
for i in range(size):
    no=int(input())
    data.append(no)


    print("enter element are:")

    for value in data:
        print(value)

Data = list()
print("Enter list:",Data)

Fdata = list(filter(checkNum,Data))
print("filter data is:",Fdata)      

Mdata = list(map(Increase,Fdata))
print("map data is:",Mdata)

Rdata = reduce(product,Mdata)
print("Reduced data is:",Rdata)




