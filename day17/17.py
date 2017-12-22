L = [0]
step = 328
curr = 0
sol = 0
for i in range(50000000):
    #insind = (L.index(i) + step + 1) % len(L)
    lenl = i+1
    insind = (curr + step + 1) % lenl #len(L)
    if insind == 0:
        #L.append(i+1)
        curr = lenl
    else:
        #L.insert(insind, i+1)
        if insind == 1:
            sol = i+1
        curr = insind
    #if i % 1000000 == 0:
    #   print(sol)
    #    print("--->", i)
    #print(L)
#print(L[L.index(2017)+1])
#print(L)
print(sol)
#print(L[(insind+1)%len(L)])