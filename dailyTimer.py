import time
import malcolm_tweet
import dropbox_ as dbx
import random

# this is the main function and scheduler
day = 86400


def main():
    dbx.download("index.txt", "index.txt")
    malcolm_tweet.main()
    dbx.upload("index.txt", "index.txt")


def getTime():
    return random.randint(day // 5, day)

counter = 0
t = getTime()
while True:

    time.sleep(1)
    if(counter % 3600 == 0):
        print("waiting...")

    counter += 1

    if counter == t:
        main()
        counter = 0
        t = getTime()
