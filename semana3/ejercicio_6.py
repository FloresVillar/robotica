import numpy as np
import ejercicio_4 
# ROT(k,theta) p = p cos + kXp sin + k k.p (1-cos) 
1
theta = np.radians(45)
p = np.array([2,1,0])
M = np.array([1,1,0])
k = M/np.linalg.norm(M)

rot = p * np.cos(theta) +  np.cross(k,p)*np.sin(theta) + k *(np.dot(k,p))*(1-np.cos(theta))

 