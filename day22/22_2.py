from sys import argv

f = open("22.txt", "r")
lines = [line.strip() for line in f.readlines()]
f.close()

grid = dict()
for i, line in enumerate(lines):
    for j, cell in enumerate(line):
        grid[(i, j)] = cell

cx, cy = (len(lines) // 2), (len(lines[0]) // 2)
d = "u"
cnt = 0
for _ in range(int(argv[1])):
    if (cx, cy) not in grid:
        cell = "."
    else:
        cell = grid[(cx, cy)]
        
    if cell == "#":
        grid[(cx, cy)] = "F"
        if d == "u":
            d = "r"
            cy += 1
        elif d == "r":
            d = "d"
            cx += 1
        elif d == "d":
            d = "l"
            cy -= 1
        elif d == "l":
            d = "u"
            cx -= 1
    elif cell == ".":
        grid[(cx, cy)] = "W"
        if d == "u":
            d = "l"
            cy -= 1
        elif d == "l":
            d = "d"
            cx += 1
        elif d == "d":
            d = "r"
            cy += 1
        elif d == "r":
            d = "u"
            cx -= 1

    elif cell == "F":
        grid[(cx, cy)] = "."
        if d == "u":
            d = "d"
            cx += 1
        elif d == "r":
            d = "l"
            cy -= 1
        elif d == "d":
            d = "u"
            cx -= 1
        elif d == "l":
            d = "r"
            cy += 1
        
    elif cell == "W":
        grid[(cx, cy)] = "#"
        cnt += 1
        if d == "u":
            cx -= 1
        elif d == "r":
            cy += 1
        elif d == "d":
            cx += 1
        elif d == "l":
            cy -= 1
            
print(cnt)