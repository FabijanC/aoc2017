f = open("19.txt", "r")
field = [line.strip("\n") for line in f.readlines()]
f.close()

##pocetak: (0, 1)

poc = tuple()
for i, el in enumerate(field[0]):
    if el == '|':
        poc = (0, i)
        break
        
seen = []
currx, curry = poc
direction = "down"
steps = 0
#while currx >= 0 and currx < len(field) and curry >= 0 and curry < len(field[0]):
while True:
    currc = field[currx][curry]
    #print(currx, curry, currc)
    if currc == " ":
        break
    elif currc.isalpha():
        seen.append(currc)
        if direction == "down":
            currx += 1
        elif direction == "up":
            currx -= 1
        elif direction == "left":
            curry -= 1
        else:
            curry += 1
    elif currc == "+":
        if direction == "down" or direction == "up":
            if field[currx][curry-1] != " ":
                curry -= 1
                direction = "left"
            elif field[currx][curry+1] != " ":
                curry += 1
                direction = "right"
        elif direction == "left" or direction == "right":
            if field[currx-1][curry] != " ":
                currx -= 1
                direction = "up"
            elif field[currx+1][curry] != " ":
                currx += 1
                direction = "down"
    
    elif direction == "down":
        currx += 1
    elif direction == "up":
        currx -= 1
    elif direction == "left":
        curry -= 1
    elif direction == "right":
        curry += 1
    else:
        print("ERR")
    # elif currc == "|":
        # if direction == "down":
            # curry += 1
        # else:
            # curry -= 1
    # if currc == "-":
        # if direction == "left":
            # curry -= 1
        # else:
            # curry += 1   
    steps += 1

print("".join(seen))
print(steps)