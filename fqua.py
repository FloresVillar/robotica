import numpy as np 
def qcongj(q):
    q = np.array(q)
    q [1:] = - q[1:]
    return q

def qprod(q1,q2):
    q1 = np.array(q1)
    q2 = np.array(q2)
    s1,v1 = q1[0],q1[1:]
    s2,v2 = q2[0],q2[1:]
    s3 = s1*s2 - np.dot(v1,v2)
    v3 = np.cross(v1,v2) + s1*v2 + s2*v1 
    return np.insert(v3,0,s3)

def qsuma(q1,q2):
    q1 = np.array(q1)
    q2 = np.array(q2)
    return q1 + q2

def qesc(n,q):
    q = np.array(q)
    return n*q

def qnorm(q):
    q = np.array(q)
    return np.sqrt(np.dot(q,q))

def qinv(q):
    q = np.array(q)
    return qconj(q)/np.dot(q,q)

#cuaternio y rotacion alrededor de k unitario(operador rotacion)
def rotk_theta(k,theta): #ejercicio1s
    # Q
    k = np.array(k)
    k_u = k /np.linalg.norm(k)
    theta = np.deg2rad(theta)
    mitad = theta/2
    s = np.cos(mitad)
    v = k_u*np.sin(mitad)
    return np.insert(v,0,s)
#aplicando esa rotacion a un vector r no unitario
def rotqr(q,r):
    # Q  (0 ,r ) Q*
    if len(q) != len(r):
        r = np.insert(r,0,0)
    res1 = qprod(q,r)
    res2 = qprod(res1,qcongj(q))
    return res2
#rotacion con traslacion 
def trasp_rotQ_movil(q,r_uvw,p):
    #Q ° (0,ruvw) ° Q* + (0,p)
    r = r_uvw
    return rotqr(q,r) + np.insert(p,0,0)

def rotQ_trasp_movil(q,r_uvw,p):
    #Q ° (0,ruvw+p) ° Q*
    r = r_uvw
    return rotqr(q,r+p)

#rotacion con traslación
def trasp_rotQ_fijo(q,r,p):
    #Q ° (0,ruvw+p) ° Q*
    return rotqr(q,r+p)

def rotQ_trasp_fijo(q,r,p):
    #Q ° (0,ruvw) ° Q* + (0,p)
    return rotqr(q,r) + np.insert(p,0,0)

def qtoH(q):
    q = np.array(q)
    q0,q1,q2,q3 = q
    H = np.array([
        [q0*q0 +q1*q1 -1/2 , q1*q2-q3*q0    , q1*q3+q2*q0     , 0],
        [q1*q2 + q3*q0     , q0**2+q2**2-1/2, q2*q3-q1*q0     , 0],
        [q1*q3-q2*q0       , q2*q3+q1*q0    , q0**2+q3**2-1/2 , 0],
        [0                 , 0              , 0               , 1/2]])
    return 2*H

#convertir H a q
def Htoq(h):
    nx,ny,nz = h[0,0],h[1,0],h[2,0]
    ox,oy,oz = h[0,1], h[1,1],h[2,1]
    ax,ay,az = h[0,2],h[1,2],h[2,2]
    q0 = 0.5*np.sqrt(nx + oy + az + 1)
    q1 = np.sign(oz - ay)*0.5*np.sqrt(nx-oy-az+1)
    q2 = np.sign(ax - nz)*0.5*np.sqrt(-nx+oy-az+1)
    q3 = np.sign(ny - ox)*0.5*np.sqrt(-nx-oy+az+1)
    return np.array([q0,q1,q2,q3])