import numpy as np

print("\nSTACKED HOPFIELD NUERAL NETWORK WEIGHTS ARE SAME PARALLEL CYCLE FUNCTION: ") 
print("\nBY MANU")
a = int(input("\nEntern the value ralted to iterate"))
m = int(input("Entern the number of row in Matrix1"))
n = int(input("Entern the number of column in Matrix1"))
Weights = []
for i in range(0, m):
    Weights.append([])
for i in range(0, m):
    for j in range(0, n):
        Weights[i].append(j)
        Weights[i][j] = 0
        print("enter row : ", i+1, "column :", j+1)
        Weights[i][j] = int(input())
print(Weights)
p = int(input("Entern the number of row in Matrix2"))
q = int(input("Entern the number of column in Matrix2"))
V = []
for i in range(0, p):
    V.append([])
for i in range(0, p):
    for j in range(0, q):
        V[i].append(j)
        V[i][j] = 0
        print("enter row : ", i+1, "column :", j+1)
        V[i][j] = int(input())
print(V)
x = int(input("Entern the number of row in Matrix3"))
y = int(input("Entern the number of column in Matrix3"))
Threshold = []
for i in range(0, x):
    Threshold.append([])
for i in range(0, x):
    for j in range(0, y):
        Threshold[i].append(j)
        Threshold[i][j] = 0
        print("enter row : ", i+1, "column :", j+1)
        Threshold[i][j] = float(input())
print(Threshold)

v = []
v.append(V)
for i in range(0, 2 ** a):
    v.append(0)
    v[i+1] = np.sign((np.dot(Weights, v[i])) - Threshold)
    z = v[i+1]
    z1 = []
    z1 = np.sign((np.dot(Weights, z)) - Threshold)
    z2 = np.sign((np.dot(Weights, z1)) - Threshold)
    diff = np.abs(z2 - V).any()
    if(diff == 0):
        #print("\ni",i+1)
        print(z2)
        #print(v[i+1])
        print("\n  Stable state")
    else:
        #print("\ni",i+1)
        print(z)
        print("\n  Unstable state")
        
#signing neuron       
print('\n\nBy: MANASA J')
input('\nPress "manu" to Exit:-')






#res = []
#for i in range(0, m):
#res.append([])
#for i in range(0, m):
#    for j in range(0,q):
#        res[i].append(j)
#        res[i][j] = 0
#for p in range(len(Weights)):
#    for q in range(len(v[0])):
#        for r in range(len(v)):
#                   res[p][q] += Weights[p][r] * v[r][q]
#print(res)
               
                              

