import math
import numpy as np

N = 1711
FB = [2, 3, 5]
def is_all_factors_in_FB(Qi : int):
    if Qi < 0:
        Qi *= -1
        vec = [1]
    else:
        vec = [0]
    for q in FB:
        index = 0
        while(Qi % q == 0):
            index += 1
            Qi /= q
        vec.append(index % 2)
    if Qi == 1:
        return np.array(vec)
    else:
        return None
    
a = [41,2,1,2,1,13,16,2,8,1,2,2,2,2,2,1,8,2,16,13,1,2,1,2,82]
p = [41,83]
for i in range(2, len(a)):
    p.append(a[i]*p[i-1]+p[i-2])
Q = []
V = []
for pi in p:
    Qi = pi ** 2 % N
    if Qi >= 2 * math.sqrt(N):
        Qi -= N
    Q.append(Qi)
    V.append(is_all_factors_in_FB(Qi))
indexs = []
for i in range(len(V)):
    if V[i] is not None:
        indexs.append(i)

def euclid(a : int,b : int) -> int:
    '''
    use euclid algorithm to calculate gcd(a,b) \n
    a >= b
    '''
    if a % b == 0:
        return b
    else:
        return euclid(b, a % b)

def is_square(v : np.array):
    v = v%2
    for d in v:
        if d != 0:
            return False
    return True

def int_to_bin(num : int, length : int):
    val = bin(num).replace('0b', '')
    for _ in range(length-len(val)):
        val = '0'+val
    comb = []
    for c in val:
        comb.append(int(c))
    return np.array(comb)

print(indexs)
completed = False
prev = np.zeros((0,4))
for i in range(1, len(indexs)):
    prev = np.concatenate((prev, V[indexs[i-1]].reshape((1,4))))
    for j in range(int(math.pow(2, i))):
        comb = int_to_bin(j, i)
        if is_square(np.dot(comb, prev)+V[indexs[i]]):
            a = np.prod(np.power(np.array([p[indexs[j]] for j in range(i)]), comb)) * p[indexs[i]] - int(np.sqrt(np.prod(np.power(np.array([Q[indexs[j]] for j in range(i)]), comb)) * Q[indexs[i]]))
            if 1 < euclid(a, N) < N:
                print(euclid(a, N))
                print([p[indexs[j]] for j in range(i)] + [p[indexs[i]]])
                print([Q[indexs[j]] for j in range(i)] + [Q[indexs[i]]])
                completed = True
                break
    if completed:
        break

