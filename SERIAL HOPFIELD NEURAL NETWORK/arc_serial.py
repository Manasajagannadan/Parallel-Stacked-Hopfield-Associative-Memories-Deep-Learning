import numpy as np
#V = np.matrix('1 -1; -1 1')
W = np.matrix('0 1 2; 1 0 3; 2 3 0')
W1 = np.matrix('0 -3 -2; -3 0 -4; -2 -4 0')
T = np.matrix('0.8 0.2 0.1; 0.5 0.9 0.7; 0.2 0.5 0.4')
v0 = []
v = np.matrix('1; -1; 1')
v0.append(v)

#print(W[0])
#print(W[1])
#print(W[2])
w =[]
w.append(W)
t = []
t.append(T)
A = np.dot(W[0], v)
n1 = np.sum(np.sign((A[0] - (t[0][0]))))
#print(t[0][1])
x = n1 * v[0]
v[0][0] = x
print("\n1st Updated Neuron", v)
#r = np.where(v>0, x, v)

#print(v)
V = []
V.append(v)
#print(V)
B = np.dot(W[1], V)
#print(B)
n2 = np.sum(np.sign((B - (t[0][1]))))
#print(n2)
x1 = np.where(v<0, n2, v)
print("\n2nd Updated Nueron", x1)
#v[1][0] = x1
C = np.dot(W[2], x1)
n3 = np.sum(np.sign((C - (t[0][2]))))
x2 = n3 * v[2]
v[2][0] = x2
x1[2][0] = x2
print("\n3rd Updated Neuron", x1)
print("\nTotal updated neuron",x1)
for i in range(0,3):
    m = (n2 - x1[1][0]).all()
    if(m == 0):
        print("\ni",i)
        print("Convergence :",x1)
        print("Stable State")
    else:
        print("Unstable State")


w1 =[]
w1.append(W1)
A1 = np.dot(W1[0], v)
n1 = np.sum(np.sign((A1[0] - (t[0][0]))))
#print(t[0][1])
x1 = n1 * v[0]
v[0][0] = x1
print("\n1st Updated Neuron", v)
#r = np.where(v>0, x, v)

#print(v)
V = []
V.append(v)
#print(V)
B = np.dot(W1[1], V)
#print(B)
n2 = np.sum(np.sign((B - (t[0][1]))))
#print(n2)
x11 = np.where(v<0, n2, v)
print("\n2nd Updated Nueron", x11)
#v[1][0] = x1
C = np.dot(W1[2], x11)
n3 = np.sum(np.sign((C - (t[0][2]))))
x21 = n3 * v[2]
v[2][0] = x21
x11[2][0] = x21
print("\n3rd Updated Neuron", x11)
print("\nTotal updated neuron",x11)
for i in range(0,3):
    m = (n2 - x11[1][0]).all()
    if(m == 0):
        print("\ni",i)
        print("Convergence :",x1)
        print("Stable State")
    else:
        print("Unstable State")
