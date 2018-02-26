import config
import malcolm_quotes as mx
import IndexReader as ir

# this is the tweeter script! it tweets to the account specified in config


def main():
    api = config.api()

    stuff = ir.main()
    pg = int(stuff[0])
    qt = int(stuff[1])

    txt = mx.getQuote(pg, qt)
    print(txt)
    api.update_status(txt)
