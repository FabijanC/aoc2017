f = open("24.txt", "r")
comps = [[int(i) for i in line.strip().split("/")] for line in f.readlines()]
f.close()

def calc(been):
    global comps
    return sum(sum(comps[li]) for li in been)

def rek(been, free):
    global comps, memo
    t = (tuple(been),free)
    if t in memo:
        return memo[t]

    sol = (len(been), calc(been))
    for i, comp in enumerate(comps):
        if i in been or free not in comp:
            continue
        nbeen = set(been)
        nbeen.add(i)
        if comp[0] == free:
            other = comp[1]
        else:
            other = comp[0]
        sol = max(sol, rek(nbeen, other))

    memo[t] = sol
    return sol

memo = dict()
globsol = (0, 0)
for i, comp in enumerate(comps):
    if 0 in comp:
        s = set()
        s.add(i)
        if comp[0] == 0:
            tmp = rek(s, comp[1])
        else:
            tmp = rek(s, comp[0])
        globsol = max(globsol, tmp)

print(globsol)