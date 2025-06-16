import threading
def Even():

    for i in range(0,21,2):
        print(i)

def odd():
    for i in range(1,21,2):
        print(i)

def main():
    T1=threading.Thread(target=Even)
    T2=threading.Thread(target=odd)
    T1.start()
    T2.start()
    T1.join()
    T2.join()

if __name__=="__main__":
    main()

    



