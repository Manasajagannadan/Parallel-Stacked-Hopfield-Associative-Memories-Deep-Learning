import numpy as np
#V = np.matrix('1 -1; -1 1')
W = np.matrix('0 1 2; 1 0 3; 2 3 0')
T = np.matrix('0.8 0.2 0.1; 0.5 0.9 0.7; 0.2 0.5 0.4')
v = np.matrix('1 1 -1; -1 1 1; 1 -1 -1')
v1 = v.transpose()
#print(v1)
v0 = []
v0.append(v1)
print(v0[0][0])
#print(W[0])
#print(W[1])
#print(W[2])
w =[]
w.append(W)
#print(w[0][2])
#print(w)
t = []
t.append(T)
for i in range(0, 3):
        A = np.dot(w[0][i], v0, out = None)
        a = []
        a.append(A)
        for k in range(0, 1):
            a.append(0)
            #print("k",k)
            print(a[k])
            for j in range(0, 1):
                n1 = np.sum(np.sign((a[k]) - (t[0][j])))
                N = []
                N.append(n1)
                for x in range(0, 1):
                        N.append(0)
                        #print(x)
                        #print(N[x])
        

        #print(a)
        #for j in range(0, 3):
         #   n1 = np.sum(np.sign((a[j]) - (t[0][j])))
            #print((W[0]) - (t[0][0]))
        #print("i",i)
        #print(n1)

            #print("i", i)
    #print(W[i])
    
    #print("i", i)
    #print(a)
    
    
    #print(n1)
    
    #if(W[i].all() == W[1].all()):
     #   s = []
     #   s.append(v)
     #   s.append(W[i])
     #   print(s))
    #for j in range(0, 3):
        
     #   print(n1)
    #A = []
    #A.append(a)
    #for j in range(0,3):
     #   A.append(0)
      #  t.append(0)
       # n1 = np.sign(a[i] - t[i][j])
        #print("j", j)
        #print(n1)
    #A = []
    #A.append(a)
    #for j in range(0, 3):
     #   A.append(0)
      #  print("i", i)
       # n1 = np.sign(A[i] - T[i])
        #print(n1)
    
    
#print(V)
#print(W)
#print(T)
#print(v)
#print(W)
#print(T)
#a = np.dot(W, v)
#print(a[0])
#print(a[0][0])
#print(a[1][0])
#print(a[2][0])
          
