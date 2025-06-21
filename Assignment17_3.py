import schedule
import time

def Myschedule():
    print("Do coding..! ")

def Main():
    schedule.every(30).minutes.do(Myschedule)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    Main()





