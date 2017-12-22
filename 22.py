f = open("22h.txt", "r")
lines = [line.strip() for line in f.readlines()]
f.close()

grid = dict()
for i, line in enumerate(lines):
    for j, cell in enumerate(line):
        grid[(i, j)] = cell

cx, cy = len(lines) // 2, len(lines([0]) // 2
d = "u"
cnt = 0
for _ in range(10000):
    if grid[(cx, cy)] == "#":
        