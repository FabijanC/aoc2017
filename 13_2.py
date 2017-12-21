def move():
    global curr, direction, range_
    
    for scanner in curr:
        
            if curr[scanner] == range_[scanner]:
                curr[scanner] -= 1
                direction[scanner] = "up"
            elif curr[scanner] == 1:
                curr[scanner] = 2
                direction[scanner] = "down"
            elif direction[scanner] == "up":
                curr[scanner] -= 1
            elif direction[scanner] == "down":
                curr[scanner] += 1
            else:
                print("ERR")
'''
        if direction[scanner] == "down":
            curr[scanner] += 1
            if curr[scanner] == range_[scanner]:
                direction[scanner] = "up"
        if direction[scanner] == "up":
            curr[scanner] -= 1
            if curr[scanner] == 1:
                direction[scanner] = "down"
'''
        
f = open("13.txt", "r")
lines = f.readlines()
f.close()

range_ = dict()
curr = dict()
direction = dict()
for line in lines:
    left, right = [int(i) for i in line.strip().split(": ")]
    range_[left] = right
    curr[left] = 1
    direction[left] = "down"

minseverity = 1
last_config = (dict(curr), dict(direction))
seen = list()
seen.append((tuple(curr.values()), tuple(direction.values())))
while True:
    #for i in curr:
    #    curr[i] = 1
    #    direction[i] = "down"
    #for _ in range(minseverity):
    #    move()

    curr = last_config[0]
    direction = last_config[1]
    move()
    last_config = (dict(curr), dict(direction))
    print(curr.values())
    #t = (tuple(curr.values()), tuple(direction.values()))
    #if t in seen:
    #    print(minseverity)
    #    break
    #else:
    #    seen.append(t)

    #if minseverity % 1000 == 0:
    #    print(minseverity)
        
    #max depth is recorded in variable left
    severity = 0
    for position in range(left + 1):
        if position in range_ and curr[position] == 1:
            ##severity += range_[position] * position
            severity = 1
            break
        move()

    if severity == 0:
        break

    minseverity += 1
    
print(minseverity)
