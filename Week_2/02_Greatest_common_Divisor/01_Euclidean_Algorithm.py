"""
if b = 0
    return a
a' -< remainder when a is divided by b
return EuclideanGCD(b, a')
"""


def EuclideanGCD(a, b):
    if b == 0:
        return a
    a_prime = b % a

    return EuclideanGCD(b, a_prime)


print("GCD: ", EuclideanGCD(3918848, 1653264))


import math

print("True GCD: ", math.gcd(3918848, 1653264))