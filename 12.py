def rek(node):
    global ajd, been
    if node in been:
        return
    been.add(node)
    for neighbor in adj[node]:
        rek(neighbor)

f = open("11.txt", "r")
lines = f.readlines()
f.close()

adj = dict()

for line in lines:
    left, right = line.strip().split("<->")
    left = left.strip()
    right = right.strip().split(", ")
    if left not in adj:
        adj[left] = right
    else:
        adj[left].extend(right)

been = set()
groups = 0
for node in adj:
    if node in been:
        continue
    groups += 1
    rek(node)

print(groups)
