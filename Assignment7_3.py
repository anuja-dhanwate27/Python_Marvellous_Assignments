def Even(no):
    return no%2==0

print("Enter the size of list:")
size= int(input())

Data = list()
print("Enter list:")
for i in range(size):
    no = int(input())
    Data.append(no)

FData=list(filter(Even,Data))
print("Even number:",FData)


