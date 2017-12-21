d0 = {"se": (+1, +1), "s": (+1, 0), "sw": (+1, -1), "nw": (0, -1), "n": (-1, 0), "ne": (0, +1)}
d1 = {"se": (0, +1), "s": (+1, 0), "sw": (0, -1), "nw": (-1, -1), "n": (-1, 0), "ne": (-1, +1)}

D = [d0, d1]

def dist(startx, starty, finalx, finaly):
    global D
    currx, curry = startx, starty
    steps = 0
    while True:
        d = D[curry % 2]
        if finalx == currx:
            return(steps + abs(curry - finaly))
            
        elif finaly == curry:
            return(steps + abs(currx - finalx))
            
        elif finalx > currx:
            side = "s"
            if finaly > curry:
                side += "e"
            else:
                side += "w"
        elif finalx < currx:
            side = "n"
            if finaly > curry:
                side += "e"
            else:
                side += "w"

        currx += d[side][0]
        curry += d[side][1]

        steps += 1


f = open("10.txt", "r")
s = f.read().strip()
f.close()

tokens = s.split(",")

been = set()

startx, starty = 1, 2
currx, curry = startx, starty
been.add((currx, curry))
for token in tokens:
    d = D[curry % 2]

    currx += d[token][0]
    curry += d[token][1]
    
    been.add((currx, curry))

finalx, finaly = currx, curry

m = max(been, key = lambda pair: dist(startx, starty, pair[0], pair[1]))

print(dist(startx, starty, m[0], m[1]))
