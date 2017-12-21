f = open("4.txt", "r")
lines = [line.strip().split() for line in f.readlines()]
f.close()

L = [2]


d = {"a": 2}

for i in range(ord("b"), ord("z")+1):
    n = L[-1] + 1
    
    while True:
        prime = True
        for j in L:
            if n % j == 0:
                prime = False
                break
        if prime:
            break
        n += 1
    L.append(n)
    d[chr(i)] = n

suma = 0

for line in lines:
    s = set()
    for word in line:
        val = 1
        for c in word:
            val *= d[c]
        s.add(val)
        
    if len(s) == len(line):
        suma += 1
print(suma)
