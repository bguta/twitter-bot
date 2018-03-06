import config
import malcolm_quotes as mx
import IndexReader as ir

charLim = 280
api = config.api()


def main():

    stuff = ir.main()
    pg = int(stuff[0])
    qt = int(stuff[1])

    txt = mx.getQuote(pg, qt)
    # print(txt)
    print("page: " + str(pg) + " Quote: " + str(qt))
    tweets = shorten(txt)
    if(div(txt) > 1):
        if (not posted(tweets)):
            api.update_status(tweets.pop(0))
            for tweet in tweets:
                ide = api.user_timeline(id=api.me().id, count=1)[0].id
                api.update_status(tweet, in_reply_to_status_id=ide)
                # print(tweet)
        else:
            main()
    else:
        if (not posted(tweets)):
            api.update_status(tweets[0])
            # print(tweet[0])
        else:
            main()


def div(txt):
    if len(txt) > charLim:
        for i in range(1, 10):
            if (len(txt) // i < 280 and len(txt) % 280 >= 40):
                return i
        raise ValueError("WTF? how long is this quote")
    return 1


def shorten(txt):
    i = div(txt)
    letters = list(txt)
    ar = []
    for j in range(i):
        q = j + 1
        t = "".join(letters[j * len(letters) // i: q * len(letters) // i])
        ar.append(t)
    return ar


def posted(txts):
    tweets = [tweet.full_text for tweet in api.user_timeline(
        id=api.me().id, count=(10 ** 4), tweet_mode="extended")]
    for tweet in tweets:
        if eq(tweet, txts[0]):
            print("Already posted")
            return True
    return False


def eq(tx1, tx2):
    if len(tx1) != len(tx2):
        return False
    if tx1 == tx2:
        return True
    return False
