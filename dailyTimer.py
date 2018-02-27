import schedule
import time
import malcolm_tweet


# this is the main function and scheduler

def main():
    malcolm_tweet.main()

# every day at 21:30 GMT lol
schedule.every().day.at("9:30").do(main)

counter = 0
while True:
    schedule.run_pending()
    time.sleep(1)
    counter += 1
    if(counter % 60 == 0):
        print("waiting...")
