f = open("6.txt", "r")
L = [int(i) for i in f.read().strip().split()]
f.close()

cycles = 0

d = dict()
t = tuple(L)
while t not in d:

    d[t] = cycles
    
    mi = 0
    for i in range(1, len(L)):
        if L[i] > L[mi]:
            mi = i

    m = L[mi]
    L[mi] = 0
    i = (mi + 1) % len(L)
    while m:
        L[i] += 1
        m -= 1
        i = (i + 1) % len(L)

    cycles += 1
    t = tuple(L)
    

print(cycles - d[tuple(L)])
