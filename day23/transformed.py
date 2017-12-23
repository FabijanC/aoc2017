a, b, c, d, e, f, g, h = 1, 0, 0, 0, 0, 0, 0, 0
b = 67
c = b
if a != 0:
    b = b * 100 + 100000
    c = b + 17000

f, d, e = 1, 2, 2
cnt = 0
while True:
    '''print("b={}, c={}, d={}, e={}, f={}, h={}".format(
        b, c, d, e, f, h)
    )'''
    # cnt += 1
    if d * e == b:
        print(c, d, e, b)
        f = 0
    e += 1
    if e != b:
        continue
    e = b
    d += 1
    # print("HERE")
    if d != b:
        e = 2
        continue
    # print("ZERE")
    if f == 0:
    #print(d, c, b)
    #if (d-1)*(e-1) == b:
        h += 1
    if b == c:
        break
    b += 17
    f, d, e = 1, 2, 2

print(h)