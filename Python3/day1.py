file = open("../Input/day1.in", "r")

freq = 0
d = []
q = {}
first = True

for i in file:
    d.append(i)

file.close()

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
    if first:
        print(freq)
        first = False
