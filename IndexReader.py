import re

# this reads the index.txt to determine which quote number to read next

# this reads the file


def look():
    with open("index.txt", "r") as file:
        line = file.readline()
        ar = re.sub(r"\t", " ", line).split()
        return ar

# this writes the file


def write(p, q):
    with open("index.txt", "w") as file:
        file.write(str(p) + "\t" + str(q))

# changes and adjusts the file and returns the page and quote numbers


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
