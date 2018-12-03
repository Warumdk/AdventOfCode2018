file = open("../Input/day3.in", "r")

fabric = []
[fabric.append([None] * 1000) for x in range(1000)]
overlap = 0
ids = {}
for l in file:
    data = l.split()
    x, y = data[2].split(",")
    y = int(y[:-1])
    x = int(x)
    z, q = [int(t) for t in data[3].split("x")]
    for i in range(x, z+x):
        for j in range(y, q+y):
            if fabric[i][j] is None:
                fabric[i][j] = [data[0]]
                if data[0] not in ids:
                    ids[data[0]] = "alone"
            elif fabric[i][j] is not None:
                fabric[i][j].append(data[0])
                ids[data[0]] = "shared"
                for d in fabric[i][j]:
                    ids[d] = "shared"
                overlap += 1

print(overlap)

for k in ids:
    if ids[k] == "alone":
        print(k[1:])

file.close()
