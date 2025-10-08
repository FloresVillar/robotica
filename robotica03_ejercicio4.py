#xyz = H @ uvw
#se tiene H
import numpy as np 
from homo4 import *
np.set_printoptions(precision = 4, suppress = True)  
H = T4(2,3,4)@Ry4(53)@Rx4(60)@Rz4(45)
print(H)
r_uvw = np.array([2,4,6,1])
r_xyz = H @ r_uvw
#volando el 1
r_xyz = r_xyz[:3]
print("\n")
print(r_xyz)