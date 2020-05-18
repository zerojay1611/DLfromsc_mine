import numpy as np

def AND(x1, x2):
    X = np.array([x1,x2])
    W = np.array([1.0, 1.0])
    b = -1.5
    tmp = np.sum(W*X) + b

    if tmp > 0:
        return 1
    else:
        return 0
def NAND(x1, x2):
    X = np.array([x1, x2])
    W = np.array([-1.0, -1.0])
    b = 1.5
    tmp = np.sum(W*X) + b

    if tmp > 0:
        return 1
    else:
        return 0
def OR(x1, x2):
    X = np.array([x1, x2])
    W = np.array([1.0, 1.0])
    b = 0
    tmp = np.sum(W*X) + b

    if tmp > 0:
        return 1
    else:
        return 0
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)

    return y

for i in range(2):
    for j in range(2):
        print('(%d, %d) : %d' %(j,i,XOR(j,i)))

