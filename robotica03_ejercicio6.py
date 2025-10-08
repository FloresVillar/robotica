#xyz = H @ uvw
#se tiene H
import numpy as np 
from homo4 import *
np.set_printoptions(precision = 4, suppress = True)  
H =Rz4(75)@Ry4(37)@Rx4(53)@T4(5,6,7)
print(H)
r_xyz = np.array([2,3,4,1])
r_xyz_prima = H @ r_xyz
#volando el 1
r_xyz_prima = r_xyz_prima[:3]
print("\n")
print(r_xyz_prima)