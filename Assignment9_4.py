import time 
import threading
import multiprocessing

def sumNumbers():
    sum = 0
    for i in range(1,10000000):
        sum = sum+1

def ByThread():
    def sum():
        sum = 0
        for i in range(1,10000000):
            sum = sum+1
    T2 = threading.Thread(target=sum)
    T2.start()
    T2.join()

def ByProcesss():
    def sum():
        sum=0
        for i in range(1,0000000):
            sun = sum+1
    P1=multiprocessing.Process(target=sum)
    P1.start()
    P1.join()

def main():
    start_time=time.time()
    T1=threading.Thread(target=sumNumbers)
    T1.start()
    T1.join()
    end_time=time.time()
    print("The sumNumbers function time is:",start_time-end_time)
   
    start_time=time.time()
    ByThread()
    end_time=time.time()
    print("the ByProcess function time is :",end_time-start_time)

    start_time=time.time()
    ByProcesss()
    end_time=time.time()
    print("The ByProcess time is :",end_time-start_time)


if __name__ == "__main__":
    main()

