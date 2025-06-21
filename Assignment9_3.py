import multiprocessing

def factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact=fact*i
    return fact

def main():
    Data=[45,67,89,90,89]
    result=[]

    P1=multiprocessing.Pool()
    result=P1.map(factorial,Data)
    P1.close()
    P1.join()

    print(result)

if __name__=="__main__":
    main()

    

