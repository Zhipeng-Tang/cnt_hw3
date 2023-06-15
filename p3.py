import math
import numpy as np

P = 50
A = 500
N = 1046603

def is_prime_number(num : int):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

FB = []
for i in range(2,P+1):
    if is_prime_number(i):
        FB.append(i)
print(FB)

length = len(FB) + 1

p = [int(math.sqrt(N))]
Q = [(int(math.sqrt(N)))**2-N]
V = []

for i in range(1, A+1):
    p.append(abs(-i+int(math.sqrt(N))))
    Q.append((-i+int(math.sqrt(N)))**2-N)
    p.append(abs(i+int(math.sqrt(N))))
    Q.append((i+int(math.sqrt(N)))**2-N)
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
        return np.array(vec, dtype=np.int64)
    else:
        return None

for Qi in Q:
    V.append(is_all_factors_in_FB(Qi))
Q = np.array(Q, dtype=np.int64)
p = np.array(p, dtype=np.int64)
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
    return np.sum(v) == 0

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
prev = np.zeros((0,length))
print([Q[indexs[i]] for i in range(len(indexs))])
print([p[indexs[i]] for i in range(len(indexs))])
# print([V[indexs[i]] for i in range(len(indexs))])
for i in range(1, len(indexs)):
    prev = np.concatenate((prev, V[indexs[i-1]].reshape((1,length))))
    for j in range(int(math.pow(2, i))):
        comb = int_to_bin(j, i)
        
        if is_square(np.dot(comb, prev)+V[indexs[i]]):
            # print(np.dot(comb, prev))
            # print(V[indexs[i]])
            # print(np.dot(comb, prev)+V[indexs[i]])
            print(comb)
            if np.prod(np.power(np.array([Q[indexs[j]] for j in range(i)]), comb)) < 0:continue
            a = np.prod(np.power(np.array([p[indexs[j]] for j in range(i)]), comb)) * p[indexs[i]] - np.int64(np.sqrt(np.prod(np.power(np.array([Q[indexs[j]] for j in range(i)]), comb)) * Q[indexs[i]]))
            if 1 < euclid(a, N) < N:
                print(euclid(a, N))
                print([p[indexs[j]] for j in range(i)] + [p[indexs[i]]])
                print([Q[indexs[j]] for j in range(i)] + [Q[indexs[i]]])
                print(comb)
                completed = True
                break
    if completed:
        break
