import schedule
import time 

def Myschedule():
    print("Namskar...")

def main():
    schedule.every().day.at("09:00:00").do(Myschedule)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()
    