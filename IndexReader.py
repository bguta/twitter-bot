import re


def look():
    with open("index.txt", "r") as file:
        line = file.readline()
        ar = re.sub(r"\t", " ", line).split()
        return ar


def write(p, q):
    with open("index.txt", "w") as file:
        file.write(str(p) + "\t" + str(q))


def main():
    reset = False
    stuff = look()
    p = int(stuff[0])
    q = int(stuff[1])

    if(p is 32 and q is 6):
        reset = True
    if(q is 25 and p < 32):
        p += 1
    if(not(p is 32)):
        q = (q % 25) + 1
    else:
        q = (q % 6) + 1

    if(reset is True):
        p = 1
    write(p, q)

    return stuff
