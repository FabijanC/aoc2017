from math import ceil, sqrt

def prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, ceil(sqrt(n)), 2):
        if n % i == 0:
            return False
    return True
cnt = 0
for x in range(106700, 123700+1, 17):
    if not prime(x):
        cnt += 1
print(cnt)