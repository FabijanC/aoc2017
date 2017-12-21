def reverse(L, curr, length):
    steps = length//2
    i = curr
    j = (curr + length - 1) % len(L)
    
    while steps:
        L[i], L[j] = L[j], L[i]
        i = (i + 1) % len(L)
        j = (j - 1) % len(L)
        steps -= 1    

##
##def to_hex(n):
##    global d
##    if n == 0:
##        return "00"
##    sol = ""
##    while n:
##        z = n % 16
##        sol = d[z] + sol
##        n //= 16
##
##    return sol if len(sol) == 2 else "0" + sol

def to_hex(n):
    sol = hex(n)[2:]
    return sol if len(sol) == 2 else "0" + sol

def to_hash(word):
    L = [i for i in range(256)]
    lengths = [ord(i) for i in s]
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

    return "".join(hex_values)

if __name__ == "__main__":
    s = "flqrgnkx-0"
    print(to_hash(s))
