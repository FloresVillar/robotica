"""
derivadas: 
"""

import numpy as np 

FACTOR = 180/np.pi

def ejercicio1():
    """ coordenadas cilindricas del punto A(-1,-1,3)
    x =-1
    y = -1
    z= 3
    r =( x^2 + y^2 )^.5
    theta = artan(y/x) ver signo
    z= z
    """
    x =-1 ;y=-1;z= 3
    r = (x**2 + y**2 )**(0.5)
    theta = np.arctan(y/x)
    pi=np.pi
    theta = theta * 180/pi
    P = {"r":r,"theta":theta,"z":z}
    return P

def ejercicio2():
    """P(r,theta,z) → P(x,y,z)
        P(2,2pi/3,-4) 
        x = r cos theta
        y = r sen theta
    """
    r = 2
    theta = 2*np.pi/3
    z = -4
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    P = {"x":x,"y":y,"z":z}
    return P

def ejercicio3():
    """coordenadas cartesianas de p(4,2pi/3,pi/6)
    """
    return None

def ejercicio4():
    """coordenadas esfericas de (-1/2,3^.5/2,3^.5)
    """
    x = -1
    y = (3**(0.5))/2
    z = 3**(0.5)
    r1 = (x**2 + y**2)/2
    theta = np.arctan(y,x)
    #z = r2 * cos (phi)
    #r1 = r2. sin(phi) 
    #r1_z = tan(phi)
    phi = np.arctan(r1,z)
    r2 = z/np.cos(phi)
    P ={"r":r2,"theta":theta*FACTOR,"phi":phi*FACTOR}
    return P

if __name__=='__main__':
    P = ejercicio4()
    print(P)
   