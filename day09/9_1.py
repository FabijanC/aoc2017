f = open("9.txt", "r")
L = f.read()
L = L.strip()

f.close()

suma = 0
i = 0
cnt = 0
gsuma = 0
garbage = False
while i < len(L):
    if L[i] == "!":
        i += 2
        continue

    if not garbage and L[i] == "<":
        garbage = True
    
    elif garbage:
        if L[i] == ">":
            garbage = False
        else:
            gsuma += 1
        i += 1
        continue

    elif L[i] == "{":
        cnt += 1

    elif L[i] == "}":
        suma += cnt
        cnt -= 1

    i += 1

print(suma)
print(gsuma)
