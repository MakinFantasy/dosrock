with open('17.txt') as f:
    n = [int(x) for x in f]

mn = min(x for x in n if x % 17 == 0)
sums = []
for a, b in zip(n, n[1:]):
    if a % mn == 0 or b % mn == 0:
        sums.append(a + b)
print(len(sums), max(sums))
