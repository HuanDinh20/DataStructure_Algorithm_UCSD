"""
Fiblist(n)
    create array F[0, ..., n]
    F[0] = 0
    F[1] = 1
    for i in range (2, n):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]
"""
