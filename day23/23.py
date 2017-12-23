f = open("23.txt", "r")
lines = [line.strip().split() for line in f.readlines()]
f.close()
regs = dict()
for r in range(ord('a'), ord('h')+1):
    regs[chr(r)] = 0
regs["a"] = 1
i = 0
cnt = 0
while i >= 0 and i < len(lines):# and cnt < 1000:
    # print(lines[i])
    if i == 11:
        print("a={}, b={}, c={}, d={}, e={}, f={}, g={}, h={}".format(
            regs["a"], regs["b"], regs["c"], regs["d"], regs["e"], regs["f"], regs["g"], regs["h"])
        )
        cnt += 1
    cmd, x, y = lines[i]
    y = regs[y] if y.isalpha() else int(y)
    if cmd == "set":
        regs[x] = y
    elif cmd == "sub":
        regs[x] -= y
    elif cmd == "mul":
        regs[x] *= y
    elif cmd == "jnz":
        x = regs[x] if x.isalpha() else int(x)
        if x != 0:
            i += y
            continue

    i += 1

print(regs["h"])