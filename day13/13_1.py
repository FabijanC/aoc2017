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

#max depth is recorded in variable left
severity = 0
for position in range(left + 1):
    if position in range_ and curr[position] == 1:
        severity += range_[position] * position
    move()

print(severity)
