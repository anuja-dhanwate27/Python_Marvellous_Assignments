from functools import reduce

def product(no1,no2):
    return no1*no2

print("Enter the size of list:")
size= int(input())

Data = list()
print("Enter list:")
for i in range(size):
    no = int(input())
    Data.append(no)

RData=reduce(product,Data)
print("Product:",RData)


