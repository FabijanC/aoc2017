from queue import Queue

class Program:
    def __init__(self, id):
        self.id = id
        self.regs = dict()
        self.regs["p"] = id
        self.i = 0
        #self.last = None
        self.q = Queue()
        self.cnt = 0
        self.lenq = 0
        self.waiting = False
        
    def simulate_one(self):
        if self.i < 0 or self.i >= len(lines):
            return
        #line = lines[self.i]
        #tokens = line.strip().split()
        tokens = lines[self.i]
        cmd = tokens[0]
        regi = tokens[1]
        val = tokens[2] if len(tokens) == 3 else None
        if val is not None:
            val = self.regs[val] if val.isalpha() else int(val)
        if regi.isalpha() and regi not in self.regs:
            self.regs[regi] = 0
        
        if cmd == "snd":
            other = programs[1-self.id]
            val = self.regs[regi] if regi.isalpha() else int(regi)
            other.q.put(val)
            self.cnt += 1
            other.lenq += 1
            
        elif cmd == "set":
            self.regs[regi] = val
        elif cmd == "add":
            self.regs[regi] += val
        elif cmd == "mul":
            self.regs[regi] *= val
        elif cmd == "mod":
            self.regs[regi] %= val
        elif cmd == "jgz":
            x = self.regs[regi] if regi.isalpha() else int(regi)
            if x > 0:
                self.i += val
                return
        elif cmd == "rcv":
            if self.q.empty():
                self.waiting = True
                #other = programs[1-self.id]
                #if other.waiting:
                #    print(programs[1].cnt)
                #    exit()
                return
            else:
                self.waiting = False
                self.regs[regi] = self.q.get()
                self.lenq -= 1
                
        self.i += 1
    
    def simulate(self):
        while self.i >= 0 and self.i < len(lines):
            self.simulate_one()
            #print(self)
            #print(programs[1-self.id])
        
    def __str__(self):
        if self.id == 0:
            return "id: {}, i: {}, cnt: {},\nregs: {}\nqlen: {}".format(self.id, self.i, self.cnt, self.regs, self.lenq)
        return "\tid: {}, i: {}, cnt: {},\n\tregs: {}\n\tqlen: {}".format(self.id, self.i, self.cnt, self.regs, self.lenq)
        
def simulate(programs):
    #while programs[0].i >= 0 and programs[0].i < len(lines) and programs[1].i >= 0 and programs[1].i < len(lines):
    while not programs[0].waiting or not programs[1].waiting:
        #print(lines[programs[0].i])
        programs[0].simulate_one()
        #print(programs[0])
        #print(lines[programs[1].i])
        programs[1].simulate_one()
        #print(programs[1])
        #print()
        
f = open("18h2.txt",  "r")
lines = [line.strip().split() for line in f.readlines()]
f.close()

programs = [Program(0), Program(1)]
simulate(programs)
print(programs[1].cnt)

#t0 = start_new_thread(programs[0].simulate, ())
#t1 = start_new_thread(programs[1].simulate, ())
#t0.join()
#t1.join()
#print(programs[1].cnt)