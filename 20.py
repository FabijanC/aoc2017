import sys

class Point:
    def __init__(self, id, p, v, a):
        self.id = id
        self.p = p
        self.v = v
        self.a = a
        self.alive = True

    def __str__(self):
        return "[id:{}, p:{}, v:{}, a:{}]".format(self.id, self.p, self.v, self.a)
        
    def move(self):
        for i in range(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]
            
    def dist_origin(self):
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])
        
class Point_list:
    def __init__(self, L=[]):
        self.L = L
    
    def add(self, point):
        self.L.append(point)
    
    def count_living(self):
        cnt = 0
        for point in self.L:
            if point.alive:
                cnt += 1
        return cnt
    
    def simulate_collisions(self, steps=1, debug=False):
        pos_dict = dict()
        for _ in range(steps):
            for point in self.L:
                if not point.alive:
                    continue
                point.move()
                t = tuple(point.p)
                if t in pos_dict:
                    pos_dict[t].append(point.id)
                else:
                    pos_dict[t] = [point.id]
                
            if debug: print(self)
    
        #removing of collided particles
        for pos in pos_dict:
            if len(pos_dict[pos]) == 1:
                continue
            for pointi in pos_dict[pos]:
                self.L[pointi].alive = False
        
    def simulate(self, steps=1, debug=False):
        for _ in range(steps):
            for point in self.L:
                point.move()
                
            if debug: print(self)
        
    def find_closest(self):
        mini = 0
        for i, point in enumerate(self.L):
            if point.dist_origin() < self.L[mini].dist_origin():
                mini = i
        
        return mini, self.L[mini].dist_origin()
        
    def __len__(self):
        return len(self.L)
        
    def __str__(self):
        tmplist = []
        for point in self.L:
            tmplist.append(str(point))
        return "{" + ", ".join(tmplist) + "}"
        
points = Point_list()
iterations = int(sys.argv[1])

f = open(sys.argv[2])
lines = f.readlines()
f.close()

index = 0
for line in lines:
    pt, vt, at = line.strip("\n").split(", ")
    p = [int(n) for n in pt.strip("p=< ").strip(">").split(",")]
    v = [int(n) for n in vt.strip("v=< ").strip(">").split(",")]
    a = [int(n) for n in at.strip("a=< ").strip(">").split(",")]
    points.add(Point(index, p, v, a))
    #print(points.L[-1])
    index += 1

points.simulate_collisions(iterations, debug=False)
#print(points.find_closest())
print(points.count_living())