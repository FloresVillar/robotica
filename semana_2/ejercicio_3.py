import numpy as np
"""
 [px,py] = R @ [pu,pv]
 R=[[cos theta,-sen theta],[sen theta,cos theta]]
    theta = 30
"""
def ejercicio_3_1():
    theta = 180*np.pi/180
    X = np.array([-3,2])
    R = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
    print(X);print(R)
    R_i = np.linalg.inv(R)
    X_rotada = R_i@np.transpose(X)
    print(X_rotada)
#####CODIGO DE PROFE
import numpy as np 
def Rz(a):
    #pasar a radianes
    a = np.radians(a)
    c = np.cos(a)
    s = np.sin(a)
    return np.array([[c,-s],
                    [s,c]])
#vector
v = np.array([-3,2])
#Roto
R=Rz(180)
v_rot = R @ v
#vector respecto al origen
v = np.array([2,-2])
c = np.array([-3,4])
#vector v respecto al nuevo origen c 
u = v - c
#rotando u 
u_rot = R(60) @ u 
#regresando al origen (0,0)

########FIN CODIGO PROFE

def traslacion(a,b)
    return a - b

def ejercicio_3_2():
    v = np.array([2,-2])
    respecto = np.array([-3,4])
    R =Rz(60)
    v_prima = (v,respecto)
    v_rotado =  R @ v_prima
    v__final = respecto + v_rotado
    print(v_final)


if __name__=='__main__':
    ejercicio_3_1()