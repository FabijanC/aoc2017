from queue import Queue
        

def reverse(L, curr, length):
    steps = length//2
    i = curr
    j = (curr + length - 1) % len(L)
    
    while steps:
        L[i], L[j] = L[j], L[i]
        i = (i + 1) % len(L)
        j = (j - 1) % len(L)
        steps -= 1    

def to_hex(n):
    sol = hex(n)[2:]
    return sol if len(sol) == 2 else "0" + sol

def to_hash(word):
    L = [i for i in range(256)]
    lengths = [ord(i) for i in word]
    lengths.extend([17, 31, 73, 47, 23])
    #lengths = [3, 4, 1, 5]
    
    curr, skip = 0, 0
    for _ in range(64):
    #print(L)
        for length in lengths:
            reverse(L, curr, length)
            curr = (curr + length + skip) % len(L)
            skip += 1
            #print(L, curr, skip)

    hex_values = []

    for i in range(16):
        t = L[i*16]
        for j in range(1, 16):
            t ^= L[i*16 + j]
        hex_values.append(to_hex(t))
    #print(hex_values)
    return "".join(hex_values)

if __name__ == "__main__":
    #s = "flqrgnkx-"
    s = "nbysizxe-"
    d = dict()
    for i in range(10):
        d[str(i)] = i
    for i in range(ord('a'), ord('f') + 1):
        d[chr(i)] = i - ord('a') + 10

    used = 0

    sol = []
    for row in range(128):
        knot_hash = to_hash(s+str(row))
        #print(s+str(row))
        #print(knot_hash)
        binr = []
        for digit in knot_hash:
            binh = bin(d[digit])[2:]
            binh = '0'*(4-len(binh)) + binh
            for x in binh:
                if x == '1':
                    used += 1
            binr.append(binh)
        sol.append("".join(binr))

    #nsol = []
    #for row in sol[:8]:
        #joined_row = "".join(row)
        #nrow = row[:8]
        #nsol.append(nrow)
        #for el in row[:8]:
        #    if el == "1":
        #        print("#", end="")
        #    else:
        #        print(".", end="")
        #print()
    print("used: ", used)

    #print(len(sol))
    #print(len(sol[0]))

    #for nrow in nsol:
    #    print (nrow)

    regions = 0
    been = set()
    q = Queue()
    for i in range(len(sol)):
        for j in range(len(sol[0])):
            if sol[i][j] == '0':
                continue
            if (i, j) in been:
                continue
            #been.add((i, j))
            q.put((i, j))
            regions += 1
            while not q.empty():
                ni, nj = q.get()
                if (ni, nj) in been:
                    continue
                been.add((ni, nj))
                if ni >= 0 and ni < len(sol) and nj >= 0 and nj < len(sol[0]):
                    if sol[ni][nj] == '0':
                        continue
                    #been.add((i, j))
                    q.put((ni-1, nj))
                    q.put((ni+1, nj))
                    q.put((ni, nj-1))
                    q.put((ni, nj+1))
    print(regions)
