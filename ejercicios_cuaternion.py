from fqua import *
from homo4 import *

def ejercicio1(u=None,theta=90):
    if u is None:
        u = np.array([3,-2,1])
    Q = rotk_theta(u,theta)
    return Q

def ejercicio2():
    r = np.array([5,2,-6])
    Q = ejercicio1()
    r_prima = rotqr(Q,r)
    return r_prima

def ejercicio3():
    h = np.array([
                [1,    0   ,      0],
                [0,1/2**0.5,-1/2**0.5],
                [0,1/2**0.5,1/2**0.5]
                ])
    return Htoq(h)

def ejercicioQtoH():
    q = np.array([0.92387953,0.38268343,0.0,0.0])
    return qtoH(q)

def ejercicio4():
    Qa =None ; Qb = None 
    k = np.array([1,0,1])
    theta = 45
    Qa = rotk_theta(k,theta)
    Ha = qtoH(Qa)
    print(f"Qa = {Qa}\n")
    print(f"Ha = {Ha}\n")
    k = np.array([1,1,0])
    theta = 30
    Qb = rotk_theta(k,theta)
    Hb = qtoH(Qb) 
    print(f"Qa = {Qb}\n")
    print(f"Hb = {Hb}\n")
    print(qprod(Qb,Qa))
    print(Hb@Ha)
    p = np.array([1,1,1])
    pa = rotqr(Qa,p)
    pb = rotqr(Qb,pa)
    print(pb)
    print(rotqr(qprod(Qb,Qa),p))

def ejercicio5():
    Ha = Rx4(90)
    Tb = T4(2,1,1)
    Qc = rotk_theta(np.array([1,1,0]),60)
    Hc = qtoH(Qc)
    Hd = qtoH(np.array([0.9659,0,0.2588,0.2588]))
    Te = T4(2,1,2)
    H = Ha@Tb@Hc@Hd@Te 
    # Xxyz = H Xuvw
    x_xyz = np.array([1,1,1,1])
    x_uvw = np.linalg.inv(H)@x_xyz
    print(x_uvw)

if __name__=='__main__':
    #Q = ejercicio1()
    #r_prima = ejercicio2()
    #print(r_prima)
    #H = ejercicio3()
    #print(H)
    #h = ejercicioQtoH()
    #print(h)
    #ejercicio4()
    ejercicio5()