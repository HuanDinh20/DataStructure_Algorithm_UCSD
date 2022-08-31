"""
Fn = {0, 1, F(n - 1) + F(n - 2)}

"""


def FibRecursive(n):
    if n <= 1:
        return n
    else:
        return FibRecursive(n - 1) + FibRecursive(n - 2)


print(FibRecursive(15))