f = open("5.txt", "r")
lines = [int(line.strip()) for line in f.readlines()]
f.close()

print("len(lines) = ", len(lines))
i = 0
steps = 0
while i >= 0 and i < len(lines):
    if lines[i] >= 3:
        t = lines[i]
        lines[i] -= 1
        i += t
    else:
        t = lines[i]
        lines[i] += 1
        i += t
    steps += 1

print(steps)
