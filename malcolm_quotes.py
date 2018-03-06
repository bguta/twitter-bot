import requests
from bs4 import BeautifulSoup as bs
import re

url = "http://www.azquotes.com/author/9322-Malcolm_X?p="

# p must be between 1 and 32: this is the page
# q must be between 1 and 25; this is the quote
# this method returns a quote by malcolm x from the url


def getQuote(p, q):
    if(p is 32):
        q = (q % 6) + 1
    if(p < 1 or p > 32):
        p = 16
    if(not(p is 32) and (q > 25 or q < 1)):
        q = 15
    page = requests.get(url + str(p))

    s = bs(page.content, "html.parser")
    qts = s.findAll("ul", {"class": "list-quotes"})[0].findAll("li")
    qt = re.sub(r"^\s+", " ", qts[q].text.strip(), flags=re.MULTILINE)
    qt = re.sub(r"\n Report", "", qt)
    qt = re.sub(r"\n", "", qt)
    qt = qt.split(". Malcolm X")[0]
    return qt
