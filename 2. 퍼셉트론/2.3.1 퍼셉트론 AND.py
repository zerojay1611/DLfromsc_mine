def AND(x1, x2):
    w1, w2, theta = 1.0, 1.0, 1.0
    tmp = w1*x1 + w2*x2
    if tmp > theta:
        return 1
    else:
        return 0

for i in range(2):
    for j in range(2):
        print('AND(%d, %d) : %d' %(j,i,AND(j,i)))
