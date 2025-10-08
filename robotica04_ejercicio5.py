import numpy as np 
from homo4 import *
np.set_printoptions(precision = 4, suppress = True)  
#H para xyz fijo
Hab = T4(3,0,0) @ Rz4(180) @ T4(0,0,2) @  
print(Hab)
Hbc = Ry4(90) @ 