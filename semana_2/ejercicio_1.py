"""
x = sin t
y = cos t
z = t^2
cilindricas : r , theta , z
                vr = dr/dt , vtheta= r d theta/dt, vz = dz/dt
esfericas : r    theta   phi
                vr = dr/dt , vtheta = r sin(phi) d theta/dt
                vphi = r d phi/dt
 """
import numpy as np
import sympy as sp
t = sp.symbols('t')
x = sp.sin(t)
y = sp.cos(t)
z = t**2
def velocidad_rectangulares():
    vx = x.diff(t)
    vy = y.diff(t)
    vz = z.diff(t)
    v = sp.Matrix([vx,vy,vz])    
    return v

def velocidad_cilindricas():
    r= x**2 + y**2
    theta = sp.atan(y/x)
    vr = r.diff(t)
    vtheta = r * theta.diff(t)
    vz = z.diff(t)                # sintaxis del profe, revisar..
    v = sp.Matrix([vr,vtheta,vz]) #sub = v.subs(t,..), evaluar = sub.evalf()
    print(v)
    r = [vr.subs({t:1}),vtheta.subs({t:1}),vz.subs({t:1})]
    return r

def velocidad_esfericas():
    """
    vr = dr/dt , 
    vtheta = r sin(phi) d theta/dt
    vphi = r d phi/dt"""
    r = x**2 + y**2 + z**2
    vr = r.diff(t)
    vtheta = r * sp.sin()

if __name__=='__main__':
    r  = velocidad_cilindricas()
    print(r)
    