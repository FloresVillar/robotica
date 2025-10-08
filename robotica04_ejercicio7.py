import numpy as np 
from homo4 import *
np.set_printoptions(precision = 4, suppress = True)  
#H para xyz fijo
H01 = Ry4(90) @ Rz4(90) @ T4(1,1,0)
print(H01)
H12 = Ry4(90) @ Rz4(90) @  T4(0.1,-0.5,0.5)
print(H12)
H23 = Ry4(-90) @ T4(0,0,-1.9)
print(H23)
H = H01 @ H12 @ H23
print(H)
#segun el profe
H01 = T4(0,1,1) @ Rz4(90) @ Rx4(90)
H12 = T4(0.5,0.1,-0,5) @ Ry4(90) @ Rz4(90)
H23 = T4()