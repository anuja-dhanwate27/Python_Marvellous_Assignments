import schedule
import time

def LunchTime():
    print("Lunch Time1")

def WrapUp():
    print("Wrap up work")


def main():
    schedule.every().day.at("13:00:00").do(LunchTime)
    schedule.every().day.at("18:00:00").do(WrapUp)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()

    




