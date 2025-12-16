f = open("aoc.txt", "r")
lines = f.readlines()
f.close()
from collections import Counter

sums = 0
for bttry_row in lines:
    bttry_row = bttry_row.splitlines()[0]
 
    iters = 0
    s = ""
    ind = 0
    while len(s) < 12 and iters < 20:
        for i in range(9, -1, -1): 
            if str(i) in bttry_row[ind:] and len(bttry_row) - bttry_row[ind:].index(str(i)) - ind - 1 >= 11 - len(s):
                s += str(i)
                ind = bttry_row[ind:].index(str(i)) + ind + 1
                break
        iters += 1

    sums += int(s)

print(sums)
