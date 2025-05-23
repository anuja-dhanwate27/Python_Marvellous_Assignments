def Increse(no):
    return no*2

print("Enter the size of list:")
size = int(input())

Data = list()
print("Enter list:")
for i in range(size):
    no = int(input())
    Data.append(no)

MData = list(map(Increse,Data))
print("Double list:",MData)

