##class hexi:
##    def __init__():
##        self.t = 0
##        self.ne = None
##        self.n = None
##        self.nw = None
##        self.se = None
##        self.s = None
##        self.sw = None

def calc2(side1, side2):
    global d
    diff =  abs(d[side1] - d[side2])
    if side1 > side2:
        d[side1] = diff
        d[side2] = 0
    else:
        d[side2] = 0
        d[side1]= diff

def calc(side1, side2, side3):
    global d
    diff = abs(d[side1] - d[side2])
    mini = min(d[side1], d[side2])
    d[side3] += mini
    if d[side1] < d[side2]:
        d[side1], d[side2] = 0, diff
    else:
        d[side2], d[side1] = 0, diff
    

f = open("10.txt", "r")
s = f.read().strip()
f.close()

tokens = s.split(",")

d = {"n": 0, "ne": 0, "nw": 0, "s": 0, "se": 0, "sw": 0}

for token in tokens:
    
    d[token] += 1

##diff = abs(d["se"] - d["sw"])
##mini = min(d["se"], d["sw"])
##d["s"] += mini
##if d["sw"] < d["se"]:
##    d["sw"], d["se"] = 0, diff
##else:
##    d["se"], d["sw"] = 0, diff
##
##diff = abs(d["ne"] - d["nw"])
##mini = min(d["ne"], d["nw"])
##d["n"] += mini
##if d["nw"] < d["ne"]:
##    d["nw"], d["ne"] = 0, diff
##else:
##    d["ne"], d["nw"] = 0, diff

calc2("n", "s")
calc2("se", "nw")
calc2("sw", "ne")

calc("se", "sw", "s")
calc("ne", "nw", "n")
calc("ne", "s", "se")
calc("nw", "s", "sw")
calc("n", "sw", "nw")
calc("se", "n", "ne")

suma = 0
suma += abs(d["n"] - d["s"])
suma += abs(d["ne"] - d["sw"])
suma += abs(d["nw"] - d["se"])

print(suma)
