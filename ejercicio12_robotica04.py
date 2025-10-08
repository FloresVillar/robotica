import numpy as np 

import homo4
def ejercicio12():
    R12 = np.array([[1,0,0],
                [0,0.5,-(3**0.5)*0.5],
                [0,(3**0.5)*0.5,0.5]])
    R13 = np.array([[0,0,-1],
                [0,1,0],
                [1,0,0]])
#R12 R23
#      R13
#R13= R12 @ R23
#R12^-1 R13 = R23
    R23 = np.linalg.inv(R12)@R13
    print(R23)

#cuaterniones
#Q = (costheta/2, kxsintheta/2,kysintheta/2,kzsintheta/2)
def ejercicio1_robotica05():
    k = np.array([3,-2,1])
    k =k/(14**0.5)
    theta = 90*np.pi/180
    theta =theta/2
    cos = np.cos(theta)
    sin = np.sin(theta)
    Q=np.array([cos,k[0]*sin,k[1]*sin,k[2]*sin])
    print(Q)

def Q(Q1,Q2):    
    """
    s : escalar 
    v : (q1 i ,q2 j,q3 k)
    """    
    s1,v1 = Q1
    s2,v2 = Q2
    s1*s2 - np.dot(v1,v2)
    np.cross(v1,v2) + s1*v2

if __name__=='__main__':
    ejercicio1_robotica05()
    