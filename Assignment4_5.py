from functools import reduce

def chkprime(num):
    
    if num >1:
        for i in range(2,num):
            if (num %i)==0:
                return False
                
        else:
             return True
        
def product(num):
    return num*2

def Maximum(x,y):
    if x > y:
        return x
    else:
        return y
    

    
        
data = list()
print("Enter the size of list:")
size = int(input())

print("Enter the values:")
for i in range(size):
    no=int(input())
    data.append(no)

Fdata = list(filter(chkprime,data))
print("filter data is",Fdata)

Mdata=list(map(product,Fdata))
print("map data is:",Mdata)

Rdata=reduce(Maximum,Mdata,)
print("Reduce data is:",Rdata)
