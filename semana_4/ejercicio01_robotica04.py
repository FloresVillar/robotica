#xyz = H @ uvw
#se tiene H
import numpy as np 
from homo4 import *
np.set_printoptions(precision = 4, suppress = True)  
#H para xyz fijo
H = T4(3,3,3)@Rx4(-90)@Ry4(-90)
#print(H)
# para movil 
H_m=Ry4(-90)@Rz4(90)@T4(3,-3,-3) #  translacion resprcto al primal
#print(H_m)
#para la regla de la mano deracha tengo al Z1 lo roto con los dedos apuntando al Z1 y el pulgar dira la rotacion en este caso en -Y
#movil 
H1 = Rz4(90)@T4(0,-3,2) #movil 
print(H1)
H2 = Rx4(-90) @ T4(3,-1,0) #movil
print(H2)
H = H1 @ Rx4(-90) @ T4(3,-1,0) #movil
print(H)