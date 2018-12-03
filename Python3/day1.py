from sys import stdin
freq = 0
d = []
q = {}

for i in stdin:
    d.append(i)


while True:
    for x in d:
        if x[0] == "+":
            freq += int(x[1:])
        else:
            freq -= int(x[1:])
        if freq in q:
            print(freq)
            exit(0)
        else:
            q[freq] = 0

