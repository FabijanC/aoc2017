class node:
    def __init__(self, name, weight, children=[], total_weight = 0):
        self.name = name
        self.weight = weight
        self.children = children
        self.total_weight = total_weight

def weight_sum(node_name):
    node = d[node_name]
    weight_list = []
    ws = 0
    for child in node.children:
        cn = d[child]
        cnw = weight_sum(child)
        weight_list.append(cnw)
        ws += cnw

    

    node.total_weight = node.weight + ws
    return node.total_weight

f = open("7.txt", "r")
lines = [line.strip() for line in f.readlines()]
f.close()

d = dict()
parent = dict()
for line in lines:
    if "->" not in line:
        name, weight = line.split()
        weight = int(weight.strip("(").strip(")"))
        d[name] = node(name, weight)
        continue

    left, right = line.split("->")
    left = left.strip()
    right = right.strip()
    name, weight = left.split()
    weight = int(weight.strip("(").strip(")"))

    right = right.split(", ")

    d[name] = node(name, weight, right)

    for n in right:
        parent[n] = name

root = None
for i in d:
    if i not in parent:
        root = i
        break

weight_sum(root)

def rek(node_name):
    node = d[node_name]
    children = node.children
    all_same = True
    for i in range(len(children)-1):
        if d[children[i]].total_weight != d[children[i+1]].total_weight:
            all_same = False
            break
    #ako su sva djeca iste tezine
    if all_same:
        print(node_name)
        for c in children:
            print(c, d[c].total_weight)
        p = d[parent[node_name]]
        pchildren = p.children
        print("parent: ", p.name)
        for c in pchildren:
            print(c, d[c].total_weight)
        return node_name

    if i == 0:
        if d[children[-1]].total_weight == d[children[0]].total_weight:
            return rek(children[1])
        return rek(children[0])

    return rek(children[i+1])

print(rek(root))

