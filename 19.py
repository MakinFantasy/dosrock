from functools import lru_cache

@lru_cache(None)
def g(a, b):
    if a + b >= 223:
        return 0
    ms = [(a*2, b), (a, b*2), (a+1,b), (a, b+1)]
    if any(g(x, y) == 0 for x, y in ms):
        return 1
    if all(g(x, y) == 1 for x, y in ms):
        return 2
    if any(g(x, y) == 2 for x, y in ms):
        return 3
    if all(g(x, y) in (1, 3) for x, y in ms):
        return 4
    

for x in range(1, 205):
    if g(17, x) == 3:
        print(3, x)


for x in range(1, 205):
    if g(17, x) == 4:
        print(4, x)