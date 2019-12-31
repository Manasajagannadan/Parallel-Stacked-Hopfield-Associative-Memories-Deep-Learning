import numpy as np
a = int(input("\nEntern the value ralted to iterate"))
m = int(input("Entern the number of row in w1"))
n = int(input("Entern the number of column in w1"))
Weights = []
for i in range(0, m):
    Weights.append([])
for i in range(0, m):
    for j in range(0, n):
        Weights[i].append(j)
        Weights[i][j] = 0
        print("enter row : ", i+1, "column :", j+1)
        Weights[i][j] = int(input())
print("weights : ", Weights)
m1 = int(input("Entern the number of row in w2"))
n1 = int(input("Entern the number of column in w2"))
Weights1 = []
for i in range(0, m1):
    Weights1.append([])
for i in range(0, m1):
    for j in range(0, n1):
        Weights1[i].append(j)
        Weights1[i][j] = 0
        print("enter row : ", i+1, "column :", j+1)
        Weights1[i][j] = int(input())
print("Weights1 : ", Weights1)
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
print("v vector", V)
p1 = int(input("Entern the number of row in v4"))
q1 = int(input("Entern the number of column in v4"))
V1 = []
for i in range(0, p1):
    V1.append([])
for i in range(0, p1):
    for j in range(0, q1):
        V1[i].append(j)
        V1[i][j] = 0
        print("enter row : ", i+1, "column :", j+1)
        V1[i][j] = int(input())
print("v1 vector", V1)
x = int(input("Entern the number of row in t4"))
y = int(input("Entern the number of column in t4"))
Threshold = []
for i in range(0, x):
    Threshold.append([])
for i in range(0, x):
    for j in range(0, y):
        Threshold[i].append(j)
        Threshold[i][j] = 0
        print("enter row : ", i+1, "column :", j+1)
        Threshold[i][j] = float(input())
print("Threshold", Threshold)

v = []
v.append(V)
for i in range(0, 2 ** a):
    v.append(0)
    v[i+1] = np.sign((np.dot(Weights, v[i])) - Threshold)
    z = v[i+1]
    z = np.sign((np.dot(Weights, z)) - Threshold)
    diff = np.abs(z - V).all()
    if(diff == 0):
        print("\ni",i+1)
        print(z)
        #print(v[i+1])
        print("\n  Stable state")
        s1 = []
        s1 = z
    else:
        print("\ni",i+1)
        print(z)
        print("\n  Unstable state")


v = []
v.append(V1)
for i in range(0, 2 ** a):
    v.append(0)
    v[i+1] = np.sign((np.dot(Weights1, v[i])) - Threshold)
    z1 = v[i+1]
    z1 = np.sign((np.dot(Weights1, z1)) - Threshold)
    s2 = []
    s2 = z1
    diff = np.abs(z1 - V).all()
    if(diff != 0):
        z2=np.sign((np.dot(Weights1, z1)) - Threshold)
        z1 = np.sign((np.dot(Weights1, z2)) - Threshold)
        diff = np.abs(z1 - V).all()
        if(diff == 0):
            print("\ni",i+1)
            print(z1)
        #print(v[i+1])
            print("\n  Stable state")
    else:
        print("\ni",i+1)
        print(z1)
        print("\n  Unstable state")


print("s1 value : ", s1)
print("s2 value : ", s2)
s = []
s.append(s1)
s.append(s2)
print("Stacked Matrix : ", s)

                         

