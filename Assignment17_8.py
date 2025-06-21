import schedule
import time

def Myschedule():
    print("checking mail...")


def main():
    schedule.every(10).seconds.do(Myschedule)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()


