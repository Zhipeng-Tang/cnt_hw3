import numpy as np
import math

n = 199843247
P=(1,1)
Q=(1,1)
a = 53
b = -53

def euclid(a : int,b : int) -> int:
    '''
    use euclid algorithm to calculate gcd(a,b) \n
    a >= b
    '''
    if a % b == 0:
        return b
    else:
        return euclid(b, a % b)

def inverse(x : int, y : int)->int:
    if y == 1:
        return 1, 1 - x
    else:
        a, b = inverse(y, x % y)
        return (b, a - int(x / y)*b)
    
while True:
    x1, y1, x2, y2 = P[0], P[1], Q[0], Q[1]
    if x1 == x2:
        if y1 == -y2:
            print('Not implentation!')
        elif euclid(n, (y1+y2)%n) == 1:
            _, inv = inverse(n, (y1+y2)%n)
            lambda_ = (3 * x1**2 + 1) * inv % n
            x3 = (lambda_**2 - x1 - x2) % n
            y3 = (lambda_ * (x1-x3) - y1) % n
            Q = (x3, y3)
        else:
            print(euclid(n, (y1+y2)%n))
            break
    elif euclid(n, (x1-x2)%n) == 1:
        _, inv = inverse(n, (x1-x2)%n)
        lambda_ = (y1-y2) * inv
        x3 = (lambda_**2 - x1 - x2) % n
        y3 = (lambda_ * (x1-x3) - y1) % n
        Q = (x3, y3)
    else:
        print(euclid(n, (x1-x2)%n))
        break
    print(Q)