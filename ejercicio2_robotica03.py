import numpy as np 
from homo4 import *
np.set_printoptions(precision = 4, suppress = True)  
H = T4(2,3,4)@Ry4(53)@Rx4(60)@Rz4(45)
print(H)
H_prima = Ry4(53)@Rx4(60)@Rz4(45)@T4(2,3,4)
print(H_prima)