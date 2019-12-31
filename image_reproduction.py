import numpy as np
from PIL import Image
from numpy import clip
from fl6 import V
import cv2
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
Weights=[[0, 2, 4, 3, 4, 6, 4, 8, 5, 6],[2, 0, 3, 4, 6, 0, 4, 0, 3, 9],[4, 3, 0, 4, 0, 5, 6, 4, 7, 5],[3, 4, 4, 0, 7, 3, 8, 4, 6, 4],[4, 6, 0, 7, 0, 6, 3, 0, 6, 4],[6, 0, 5, 3, 6, 0, 4, 2, 2, 4],[4, 4, 6, 8, 3, 4, 0, 4, 8, 9],[8, 0, 4, 4, 0, 2, 4, 0, 6, 7],[5, 3, 7, 6, 6, 2, 8, 6, 0, 4],[6, 9, 5, 4, 4, 4, 9, 7, 4, 0]]
print("weights : ", Weights)
print("value matrix:",V)
Threshold=[[0.1,0.2,0.3,0.4,0.5,0.2,0.4,0.2,0.5,0.6],[0.5,0.3,0.2,0.1,0.4,0.5,0.3,0.4,0.5,0.6],[0.9,0.1,0.3,0.2,0.7,0.5,0.3,0.2,0.1,0.4],[0.8,0.7,0.6,0.1,0.2,0.1,0.2,0.3,0.4,0.5],[0.1,0.2,0.1,0.2,0.3,0.4,0.5,0.3,0.5,0.4],[0.3,0.4,0.2,0.4,0.2,0.5,0.6,0.7,0.4,0.9],[0.1,0.2,0.3,0.9,0.1,0.3,0.2,0.7,0.4,0.5],[0.4,0.5,0.7,0.8,0.2,0.9,0.1,0.3,0.2,0.7],[0.1,0.3,0.7,0.8,0.2,0.9,0.1,0.5,0.6,0.7],[0.1,0.3,0.7,0.8,0.2,0.9,0.1,0.5,0.7,0.5]]
print("threshold matrix:", Threshold)
v=[]
v.append(V)
for i in range(0, 2 **10):
    v.append(0)
    v[i+1] = np.sign((np.dot(Weights, v[i])) - Threshold)
    z = v[i+1]
    z = np.sign((np.dot(Weights, z)) - Threshold)
    diff = np.abs(z - V).any()
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
z=[[-1 , 1 ,-1, -1, -1, -1, -1, -1, -1, -1]
 ,[-1, -1, -1, -1, -1, -1,  1, -1, -1, -1]
 ,[-1, -1, -1,  1 , 1, -1, -1, -1, -1, -1]
 ,[-1,  1,  1,  1,  1,  1,  1 ,-1, -1, -1]
 ,[ 1,  1,  1,  1,  1,  1,  1, -1, -1, -1]
 ,[ 1,  1,  1,  1,  1,  1,  1 ,-1, -1, -1]
 ,[-1,  1,  1,  1,  1,  1,  1, -1, -1, -1]
 ,[-1,  1,  1,  1, 1, 1,  1,  1, -1, -1]
 ,[-1, -1,  1,  1,  1,  1,  1, -1, -1, -1]
 ,[-1, -1, -1, -1, -1 ,-1, -1, -1, -1, -1]]

print('final state',z)
iar=np.where(z==-1,0,z)
iar1=np.where(iar==1,255,iar)
print(iar1)
    
import matplotlib 
matplotlib.image.imsave('applenewbw.jpg',iar1) 
                         
