import numpy as np
#V = np.matrix('1 -1; -1 1')
#W = np.matrix('0 1 2; 1 0 3; 2 3 0')
#T = np.matrix('0.8 0.2 0.1; 0.5 0.9 0.7; 0.2 0.5 0.4')
m = int(input("Entern the number of row in w1"))
n = int(input("Entern the number of column in w1"))
W = []
for i in range(0, m):
    W.append([])
for i in range(0, m):
    for j in range(0, n):
        W[i].append(j)
        W[i][j] = 0
        print("enter row : ", i+1, "column :", j+1)
        W[i][j] = int(input())
print("eights : ", W)
p = int(input("Entern the number of row in v3"))
q = int(input("Entern the number of column in v3"))
V = []
for i in range(0, p):
    V.append([])
for i in range(0, p):
    for j in range(0, q):
        V[i].append(j)
        V[i][j] = 0
        print("enter row : ", i+1, "column :", j+1)
        V[i][j] = int(input())
print("v matrix", V)
v0 = []
v = np.matrix('1; -1; 1')
v0.append(v)
x = int(input("Entern the number of row in t4"))
y = int(input("Entern the number of column in t4"))
T = []
for i in range(0, x):
    T.append([])
for i in range(0, x):
    for j in range(0, y):
        T[i].append(j)
        T[i][j] = 0
        print("enter row : ", i+1, "column :", j+1)
        T[i][j] = float(input())
print("T", T)



#print(W[0])
#print(W[1])
#print(W[2])
w =[]
w.append(W)
t = []
t.append(T)
A = np.dot(W[0], v)
n1 = np.sum(np.sign((A[0] - (t[0][0]))))
print(t[0][0])
#print(n1)
x = n1 * v[0]
v[0][0] = x
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
#print(x1)
#v[1][0] = x1
C = np.dot(W[2], x1)
n3 = np.sum(np.sign((C - (t[0][2]))))
x2 = n3 * v[2]
v[2][0] = x2
x1[2][0] = x2
print(x1)
for i in range(0,3):
    m = (n2 - x1[1][0]).all()
    if(m == 0):
        print("i",i)
        print(x1)
        print("stable")
    else:
        print("unstable")





