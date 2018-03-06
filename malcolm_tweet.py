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
    if(div(txt) > 1):
        tweets = shorten(txt)
        if (not posted(tweets)):
            api.update_status(tweets.pop(0))
            for tweet in tweets:
                ide = api.user_timeline(id=api.me().id, count=1)[0].id
                api.update_status(tweet, in_reply_to_status_id=ide)
                # print(tweet)
        else:
            main()
    else:
        tweet = shorten(txt)
        if (not posted(tweet)):
            api.update_status(txt)
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
        id=api.me().id, count=10, tweet_mode="extended")]
    for tweet in tweets:
        for txt in txts:
            if txt == tweet:
                print("YES")
                return True
    return False
