from copy import deepcopy
from sys import argv
#M = [".#.", "..#", "###"]
M = [['.', '#', '.']
    ,['.', '.', '#']
    ,['#', '#', '#']
    ]

def addperms(lm, rm, patterns):
    patterns[lm] = rm
    if len(lm) % 2 == 0:
        newm = []
        for x in range(2):
            nr = []
            for y in range(2):
                nr.append(lm[1-x][y])
            newm.append(tuple(nr))
        patterns[tuple(newm)] = rm

        newm = []
        for x in range(2):
            nr = []
            for y in range(2):
                nr.append(lm[x][1-y])
            newm.append(tuple(nr))
        patterns[tuple(newm)]  = rm

        newm = []
        for x in range(2):
            nr = []
            for y in range(2):
                nr.append(lm[1-x][1-y])
            newm.append(tuple(nr))
        patterns[tuple(newm)]  = rm

        newm = []
        for x in range(2):
            nr = []
            for y in range(2):
                nr.append(lm[y][x])
            newm.append(tuple(nr))
        patterns[tuple(newm)]  = rm

        newm = []
        for x in range(2):
            nr = []
            for y in range(2):
                nr.append(lm[1-y][x])
            newm.append(tuple(nr))
        patterns[tuple(newm)]  = rm

        newm = []
        for x in range(2):
            nr = []
            for y in range(2):
                nr.append(lm[y][1-x])
            newm.append(tuple(nr))
        patterns[tuple(newm)] = rm

        newm = []
        for x in range(2):
            nr = []
            for y in range(2):
                nr.append(lm[1-y][1-x])
            newm.append(tuple(nr))
        patterns[tuple(newm)] = rm
        
    else:
        newm = []
        for x in range(3):
            nr = []
            for y in range(3):
                nr.append(lm[2-x][y])
            newm.append(tuple(nr))
        patterns[tuple(newm)] = rm

        newm = []
        for x in range(3):
            nr = []
            for y in range(3):
                nr.append(lm[x][2-y])
            newm.append(tuple(nr))
        patterns[tuple(newm)] = rm

        newm = []
        for x in range(3):
            nr = []
            for y in range(3):
                nr.append(lm[2-x][2-y])
            newm.append(tuple(nr))
        patterns[tuple(newm)] = rm

        newm = []
        for x in range(3):
            nr = []
            for y in range(3):
                nr.append(lm[y][x])
            newm.append(tuple(nr))
        patterns[tuple(newm)] = rm

        newm = []
        for x in range(3):
            nr = []
            for y in range(3):
                nr.append(lm[2-y][x])
            newm.append(tuple(nr))
        patterns[tuple(newm)] = rm

        newm = []
        for x in range(3):
            nr = []
            for y in range(3):
                nr.append(lm[y][2-x])
            newm.append(tuple(nr))
        patterns[tuple(newm)] = rm

        newm = []
        for x in range(3):
            nr = []
            for y in range(3):
                nr.append(lm[2-y][2-x])
            newm.append(tuple(nr))
        patterns[tuple(newm)] = rm        
    
def match2(sx, sy, patterns):
    global M
    newm = []
    for x in range(2):
        nr = []
        for y in range(2):
            nr.append(M[sx+x][sy+y])
        newm.append(tuple(nr))
    return patterns[tuple(newm)]
    
def match3(sx, sy, patterns):
    global M
    newm = []
    for x in range(3):
        nr = []
        for y in range(3):
            nr.append(M[sx+x][sy+y])
        newm.append(tuple(nr))
    return patterns[tuple(newm)]
    
def newoldmatch2(sx, sy, patterns):
    global M
    
    for op, os in patterns:
        #same
        err = False
        for x in range(2):
            for y in range(2):
                if M[sx+x][sy+y] != op[x][y]:
                    err = True
                    break
        if err: break
        if not err: return deepcopy(os)
    
        #rot
        err = False
        for x in range(2):
            for y in range(2):
                if M[sx+x][sy+y] != op[1-x][1-y]:
                    err = True
                    break
        if err: break
        if not err: return deepcopy(os)
    
        #rot
        err = False
        for x in range(2):
            for y in range(2):
                if M[sx+x][sy+y] != op[1-x][y]:
                    err = True
                    break
        if err: break
        if not err: return deepcopy(os)
    
        #rot
        err = False
        for x in range(2):
            for y in range(2):
                if M[sx+x][sy+y] != op[x][1-y]:
                    err = True
                    break
        if err: break
        if not err: return deepcopy(os)
    
        #rot
        err = False
        for x in range(2):
            for y in range(2):
                if M[sx+x][sy+y] != op[y][x]:
                    err = True
                    break
        if err: break
        if not err: return deepcopy(os)
    
        #rot
        err = False
        for x in range(2):
            for y in range(2):
                if M[sx+x][sy+y] != op[1-y][1-x]:
                    err = True
                    break
        if err: break
        if not err: return deepcopy(os)
    
        #rot
        err = False
        for x in range(2):
            for y in range(2):
                if M[sx+x][sy+y] != op[1-y][x]:
                    err = True
                    break
        if err: break
        if not err: return deepcopy(os)
    
        #rot
        err = False
        for x in range(2):
            for y in range(2):
                if M[sx+x][sy+y] != op[y][1-x]:
                    err = True
                    break
        if err: break
        if not err: return deepcopy(os)
    
def oldmatch2(sx, sy, patterns):
    global M
    #Mo = [M[sx][sy], M[sx][sy+1], M[sx+1][sy], M[sx+1][sy+1]]
    Mo = []
    for x in range(sx, sx+2):
        for y in range(sy, sy+2):
            Mo.append(M[x][y])
            
    for op, os in patterns:
        #same
        if Mo == [op[0][0], op[0][1], op[1][0], op[1][1]]:
            return deepcopy(os)
        #rotcw
        if Mo == [op[1][0], op[0][0], op[0][1], op[1][1]]:
            return deepcopy(os)
        #rotcw x 2
        if Mo == [op[1][1], op[1][0], op[0][1], op[0][0]]:
            return deepcopy(os)
        #rotccw
        if Mo == [op[0][1], op[1][1], op[0][0], op[1][0]]:
            return deepcopy(os)
        #flip up-down
        if Mo == [op[1][0], op[1][1], op[0][0], op[0][1]]:
            return deepcopy(os)
        #flip left-right
        if Mo == [op[0][1], op[0][0], op[1][1], op[1][0]]:
            return deepcopy(os)
        #new1
        if Mo == [op[1][1], op[0][1], op[1][0], op[0][0]]:
            return deepcopy(os)
        #new2
        if Mo == [op[0][0], op[1][0], op[0][1], op[1][1]]:
            return deepcopy(os)
    
def newoldmatch3(sx, sy, patterns):
    global M
    for op, os in patterns:
        #same
        err = False
        for x in range(3):
            for y in range(3):
                print(op[x][y], end="")
                if M[sx+x][sy+y] != op[x][y]:
                    err = True
                    break
            print()
            if err: break
        if not err: return deepcopy(os)
    
        #rot
        err = False
        for x in range(3):
            for y in range(3):
                print(op[2-x][2-y], end="")
                if M[sx+x][sy+y] != op[2-x][2-y]:
                    err = True
                    break
            print()
            if err: break
        if not err: return deepcopy(os)
    
        #rot
        err = False
        for x in range(3):
            for y in range(3):
                if M[sx+x][sy+y] != op[2-x][y]:
                    err = True
                    break
            if err: break
        if not err: return deepcopy(os)
    
        #rot
        err = False
        for x in range(3):
            for y in range(3):
                if M[sx+x][sy+y] != op[x][2-y]:
                    err = True
                    break
            if err: break
        if not err: return deepcopy(os)
    
        #rot
        err = False
        for x in range(3):
            for y in range(3):
                if M[sx+x][sy+y] != op[y][x]:
                    err = True
                    break
            if err: break
        if not err: return deepcopy(os)
    
        #rot
        err = False
        for x in range(3):
            for y in range(3):
                if M[sx+x][sy+y] != op[2-y][2-x]:
                    err = True
                    break
            if err: break
        if not err: return deepcopy(os)
    
        #rot
        err = False
        for x in range(3):
            for y in range(3):
                if M[sx+x][sy+y] != op[2-y][x]:
                    err = True
                    break
            if err: break
        if not err: return deepcopy(os)
    
        #rot
        err = False
        for x in range(3):
            for y in range(3):
                if M[sx+x][sy+y] != op[y][2-x]:
                    err = True
                    break
            if err: break
        if not err: return deepcopy(os)
    
def oldmatch3(sx, sy, patterns):
    global M
    #Mo = [M[sx][sy], M[sx][sy+1], M[sx][sy+2], M[sx+1][sy], M[sx+1][sy+1], M[sx+1][sy+2], M[sx+2][sy], M[sx+2][sy+1], M[sx+2][sy+2]]
    Mo = []
    for x in range(sx, sx+3):
        for y in range(sy, sy+3):
            Mo.append(M[x][y])
    for op, os in patterns:
        '''
        print(":")
        printml([op[0][0], op[0][1], op[0][2], op[1][0], op[1][1], op[1][2], op[2][0], op[2][1], op[2][2]])
        print()
        printml([op[0][2], op[1][2], op[2][2], op[0][1], op[1][1], op[2][1], op[0][0], op[1][0], op[2][0]])
        print()
        printml([op[2][0], op[1][0], op[0][0], op[2][1], op[1][1], op[0][1], op[2][2], op[1][2], op[0][2]])
        print()
        printml([op[2][2], op[2][1], op[2][0], op[1][2], op[1][1], op[1][0], op[0][2], op[0][1], op[0][0]])
        print()
        printml([op[0][2], op[0][1], op[0][0], op[1][2], op[1][1], op[1][0], op[2][2], op[2][1], op[2][0]])
        print()
        printml([op[2][0], op[2][1], op[2][2], op[1][0], op[1][1], op[1][2], op[0][0], op[0][1], op[0][2]])
        print("\n")
        '''
        #same
        if Mo == [op[0][0], op[0][1], op[0][2], op[1][0], op[1][1], op[1][2], op[2][0], op[2][1], op[2][2]]:
            return deepcopy(os)
        if Mo == [op[0][2], op[1][2], op[2][2], op[0][1], op[1][1], op[2][1], op[0][0], op[1][0], op[2][0]]:
            return deepcopy(os)
        if Mo == [op[2][0], op[1][0], op[0][0], op[2][1], op[1][1], op[0][1], op[2][2], op[1][2], op[0][2]]:
            return deepcopy(os)
        #rotx2
        if Mo == [op[2][2], op[2][1], op[2][0], op[1][2], op[1][1], op[1][0], op[0][2], op[0][1], op[0][0]]:
            return deepcopy(os)
        #flip left-right
        if Mo == [op[0][2], op[0][1], op[0][0], op[1][2], op[1][1], op[1][0], op[2][2], op[2][1], op[2][0]]:
            return deepcopy(os)
        #flip up-down
        if Mo == [op[2][0], op[2][1], op[2][2], op[1][0], op[1][1], op[1][2], op[0][0], op[0][1], op[0][2]]:
            return deepcopy(os)
        #new1
        if Mo == [op[2][2], op[1][2], op[0][2], op[2][1], op[1][1], op[0][1], op[2][0], op[1][0], op[0][0]]:
            return deepcopy(os)
        #new2
        if Mo == [op[0][0], op[1][0], op[2][0], op[0][1], op[1][1], op[2][1], op[0][2], op[1][2], op[2][2]]:
            return deepcopy(os)
        '''
    print(":::::::::::::")
    printml([M[0][0], M[0][1], M[0][2], M[1][0], M[1][1], M[1][2], M[2][0], M[2][1], M[2][2]])
    print()
    printml([M[0][2], M[1][2], M[2][2], M[0][1], M[1][1], M[2][1], M[0][0], M[1][0], M[2][0]])
    print()
    printml([M[2][0], M[1][0], M[0][0], M[2][1], M[1][1], M[0][1], M[2][2], M[1][2], M[0][2]])
    print()
    printml([M[2][2], M[2][1], M[2][0], M[1][2], M[1][1], M[1][0], M[0][2], M[0][1], M[0][0]])
    print()
    printml([M[0][2], M[0][1], M[0][0], M[1][2], M[1][1], M[1][0], M[2][2], M[2][1], M[2][0]])
    print()
    printml([M[2][0], M[2][1], M[2][2], M[1][0], M[1][1], M[1][2], M[0][0], M[0][1], M[0][2]])
    print("\n")
        '''
        
        
def count_on():
    global M
    cnt = 0
    for row in M:
        for c in row:
            if c == "#":
                cnt += 1
    return cnt

def printml(l):
    if len(l) % 3 == 0:
        for i in range(0, len(l), 3):
            print("".join(l[i:i+3]))
    else:
        for i in range(0, len(l), 2):
            print("".join(l[i:i+2]))
    
def printm(m):
    for r in m:
        print("".join(r))
        
    
def main():
    global M
    iterations = int(argv[1])
    f = open("21.txt", "r")
    lines = f.readlines()
    f.close()
    #patterns2, patterns3 = [], []
    patterns = dict()
    for line in lines:
        left, right = line.strip("\n").split(" => ")
        lrows = left.split("/")
        lm = tuple((tuple(row) for row in lrows))
        rrows = right.split("/")
        rm = tuple((tuple(row) for row in rrows))
        addperms(lm, rm, patterns)
    '''for pattern in patterns:
        for r in pattern:
            print("".join(r))
        printm(patterns[pattern])
        print()'''
    for iteration in range(iterations):
        print(iteration, "M: ")
        printm(M)
        print()
        newM = []
        if len(M) % 2 == 0:
            for r in range(0, len(M), 2):
                newR = [[] for _ in range(3)]
                for c in range(0, len(M[0]), 2):
                    res = (match2(r, c, patterns))
                    for i in range(3):
                        newR[i].extend(res[i])
                for rr in newR:
                    newM.append(rr)
            
        else:
            for r in range(0, len(M), 3):
                newR = [[] for _ in range(4)]
                for c in range(0, len(M[0]), 3):
                    res = (match3(r, c, patterns))
                    for i in range(4):
                        newR[i].extend(res[i])
                for rr in newR:
                    newM.append(rr)

        M = newM

    printm(M)
    print(count_on())
    
if __name__ == "__main__":
    main()
