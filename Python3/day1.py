file = open("../Input/day1.in", "r")

freq = 0
data = []
seen = {}

for i in file:
    data.append(i)

file.close()
print(sum([int(x) for x in data]))

while True:
    for x in data:
        freq += int(x)
        if freq in seen:
            print(freq)
            exit(0)
        else:
            seen[freq] = 0
