import schedule
import time
def Myschedule():
    print("jay Ganesh")
    

def main():
    schedule.every(2).seconds.do(Myschedule)
    while True:
     schedule.run_pending()
     time.sleep(1)
    
    


if __name__ =="__main__":
    main()





