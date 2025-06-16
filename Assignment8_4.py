import threading

def small(ch):
    count = 0
    for i in ch:
        if i.islower():
            count = count+1

    print("The number of small latter in string is:",count)
    print("Thread Id of thread is:",threading.get_ident())
    print("The name of curent thread is :",threading.current_thread())

def Capital(ch):
    count = 0
    for i in ch:
        if i.isupper():
            count=count+1
    print("The number of capital letter in string is:",count)
    print("Thread ID of thread is:",threading.get_ident())
    print("The name of curent thread is:",threading.current_thread())

def Digit(ch):
    count = 0
    for i in ch:
        if i.isdigit():
            count = count+1

    print("The digits in string are:",count)
    print("Thread ID of thread is :",threading.get_ident())
    print("The name of curent thread is :",threading.current_thread())

def main():
    print("Enter input:")
    str = input()
    T1=threading.Thread(target=small,args=(str,))
    T2=threading.Thread(target= Capital,args=(str,))
    T3=threading.Thread(target=Digit,args=(str,))



    T1.start()
    T2.start()
    T3.start()

if __name__ =="__main__":
    main()
    
    
