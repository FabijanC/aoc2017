#f = open("16h.txt", "r")
f = open("16.txt", "r")
moves = f.read().strip().split(",")
f.close()

L = [chr(i) for i in range(ord('a'), ord('p')+1)]
#L = [chr(i) for i in range(ord('a'), ord('e')+1)]
lenl = len(L)
pos = dict()
for i, el in enumerate(L):
    pos[L[i]] = i

seen = set()
seenl = list()
t = tuple(L)
while t not in seen:
    seen.add(t)
    seenl.append(t)
    for move in moves:
        #print(move)
        letter, rest = move[0], move[1:]
        if letter == 's':
            d = len(L) - int(rest)
            L = L[d:] + L[:d]
            n = int(rest)
            for j, el in enumerate(L):
                pos[el] = j
            #for j in range(n):
            #    L[j], L[lenl-j-1] = L[lenl-j-1], L[j]
            #    pos[L[j]] = j
            #    pos[L[lenl-j-1]] = lenl-j-1
        elif letter == 'x':
            left, right = rest.split("/")
            left, right = int(left), int(right)
            L[left], L[right] = L[right], L[left]
            pos[L[left]] = left
            pos[L[right]] = right
        elif letter == 'p':
            left, right = rest.split("/")
            #l, r = L.index(left), L.index(right)
            l, r = pos[left], pos[right]
            L[l], L[r] = L[r], L[l]
            pos[left] = r
            pos[right] = l
    
    t = tuple(L)
    #if i % 100000000 == 0:
    #    print(i)
        #print(pos)
        
print("".join(seenl[1000000000 % len(seen)]))