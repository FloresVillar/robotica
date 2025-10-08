import numpy as np 
np.set_printoptions(precision = 4, suppress = True)
def Rx(a):
    a = np.radians(a)
    c = np.cos(a)
    s = np.sin(a)
    return np.array([[1,0,0],
                    [0,c,-s],
                    [0,s,c]])
            
def Ry(a):
    a = np.radians(a)
    c = np.cos(a)
    s = np.sin(a)
    return np.array([[c,0,s],
                    [0,1,0],
                    [-s,0,c]])

def Rz(a):
    a = np.radians(a)
    c = np.cos(a)
    s = np.sin(a)
    return np.array([[c,-s,0],
                    [s,c,0],
                    [0,0,1]])

v = np.array([2,3,4])  # thetax = 37 , thetay = 53, thetaz = -90
v_final = Rz(-90) @ Ry(53) @ Rx(37) @ v
print(v_final) 
# segun profe 
