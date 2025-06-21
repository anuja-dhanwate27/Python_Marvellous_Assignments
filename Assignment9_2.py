import multiprocessing
def square(data):
    for i in data:
        square=i**2
        print("The square of",i,"is:",square)

def main():
    Data1=[12,13,14,15]
    Data2=[23,24,25,26]
    Data3=[34,35,36,37]
    P1=multiprocessing.Process(target=square,args=(Data1,))
    P2=multiprocessing.Process(target=square,args=(Data2,))
    P3=multiprocessing.Process(target=square,args=(Data3,))

    P1.start()
    P2.start()
    P3.start()
    P1.join()
    P2.join()
    P3.join()

if __name__=="__main__":
    main()


    
