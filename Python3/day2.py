from sys import stdin
from collections import Counter

twos, trees = 0, 0
data = []

for l in stdin:
    data.append(l.strip())
    c = Counter(l.strip())
    d = set(c.values())
    if 2 in d:
        twos += 1
    if 3 in d:
        trees += 1

print(twos * trees)

data.sort()

for i in range(len(data)-1):
    out, x, y, free = "", list(data[i]), list(data[i+1]), 1
    for j in range(len(x)):
        if x[j] == y[j]:
            out += x[j]
        elif x[j] != y[j] and free == 1:
            free = 0
        elif x[j] != y[j] and free == 0:
            out = ""
            break
    if out != "":
        print(out)
        break

