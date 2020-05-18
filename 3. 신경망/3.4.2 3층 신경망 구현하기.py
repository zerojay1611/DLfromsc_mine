import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def identity_function(x):
    return x
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)   #오버플로우 방지
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y
def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['B1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['B2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['B3'] = np.array([0.1, 0.2])

    return network
def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['B1'], network['B2'], network['B3']

    A1 = np.dot(x, W1) + b1
    Z1 = sigmoid(A1)

    A2 = np.dot(Z1, W2) + b2
    Z2 = sigmoid(A2)

    A3 = np.dot(Z2, W3) + b3
    y = identity_function(A3)

    return y

network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)