import schedule
import time
import malcolm_tweet


# this is the main function and scheduler

def main():
    malcolm_tweet.main()

# every day at 21:30 GMT
schedule.every().day.at("21:30").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
