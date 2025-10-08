import numpy as np 
from homo4 import *
np.set_printoptions(precision = 4, suppress = True)  
#H para xyz fijo
H12 = Rz4(90)@T4(0,-3,2) #movil 
print(H12)
H23 = Rx4(-90) @ T4(3,-1,0) #movil
print(H23)
H = H12 @ Rx4(-90) @ T4(3,-1,0) #movil
print(H)
p2 = np.array([0,2,1,1])
p1 = H12 @ p2 
p1= p1[:3]
print(p1)
p3=np.linalg.inv(H23)@ p2
p3=p3[:3]
print(p3)  
