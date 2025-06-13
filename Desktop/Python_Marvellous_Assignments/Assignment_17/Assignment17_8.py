import schedule
import time

def Job():
    print("Checking mail...")

def main():
    
    schedule.every(10).seconds.do(Job)

    print("Application is in waiting state")
    while True:
        schedule.run_pending()
        time.sleep(1)
    



if __name__ == "__main__":
    main()