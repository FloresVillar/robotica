from fqua import *

def ejercicio1(u=None,theta=90):
    if u is None:
        u = np.array([3,-2,1])
    Q = qrotk(u,theta)
    return Q

def ejercicio2():
    r = np.array([5,2,-6])
    Q = ejercicio1()
    r_prima = qrotqr(Q,r)
    return r_prima
#rotacion de r aplicando un cuternio
def no_conocido_2():
    r = np.array([5,6,7])
    print()
    #ejercicio3
    Q3 = np.array([0.9238,0.3826,0,0])
    print(qtoH(Q3))

if __name__=='__main__':
    #Q = ejercicio1()
    r_prima = ejercicio2()
    print(r_prima)