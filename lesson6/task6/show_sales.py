from sys import argv
from itertools import islice

with open('bakery.csv') as f:
    if len(argv) == 1:
        for line in f:
            print(line.strip())
    elif len(argv) == 2:
        for line in islice(f, int(argv[1]) - 1, None):
            print(line.strip())
    elif len(argv) == 3:
        for line in islice(f, int(argv[1]) - 1, int(argv[2])):
            print(line.strip())
