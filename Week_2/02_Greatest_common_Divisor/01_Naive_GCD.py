"""
************* Naive GCDs
best = 0
for d in range(1, a + b):
    if d/a and d/b:
        best = d
return best
"""


def gcd(a, b):
    best = 0
    for d in range(1, a + b):
        if a % d == 0 and b % d == 0:
            best = d
    return best


print(gcd(4, 10))
