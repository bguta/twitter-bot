import config
import malcolm_quotes as mx
import IndexReader as ir

charLim = 280


def main():
    api = config.api()

    stuff = ir.main()
    pg = int(stuff[0])
    qt = int(stuff[1])

    txt = mx.getQuote(pg, qt)
    print(txt)
    if(div(txt) > 1):
        tweets = shorten(txt)
        api.update_status(tweets.pop(0))
        for tweet in tweets:
            ide = api.user_timeline(id=api.me().id, count=1)[0].id
            api.update_status(tweet, in_reply_to_status_id=ide)

    else:
        api.update_status(txt)


def div(txt):
    if len(txt) > charLim:
        for i in range(1, 10):
            if len(txt) // i <= 280:
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
