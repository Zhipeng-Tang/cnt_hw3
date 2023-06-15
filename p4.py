import numpy as np

# n = 8051
# def f(x : int)->int:
#     return (x ** 2 + 1) % n
n = 2701
def f(x : int)->int:
    return (x * x * x + x + 1) % n

def euclid(a : int,b : int) -> int:
    '''
    use euclid algorithm to calculate gcd(a,b) \n
    a >= b
    '''
    if a % b == 0:
        return b
    else:
        return euclid(b, a % b)

x = [1]
k = 1
while True:
    x.append(f(x[k-1]))
    j = np.power(2, int(np.log(k)/np.log(2)))-1
    # print(x)
    # print(n, abs(x[k]-x[j]))
    if 1 < euclid(n, abs(x[k]-x[j])) < n:
        print(euclid(n, abs(x[k]-x[j])))
        break
    k += 1
