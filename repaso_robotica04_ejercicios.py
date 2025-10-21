import numpy as np 
np.set_printoptions(precision = 4,suppress = True)
def Rx4(a):
    a = np.radians(a)
    c = np.cos(a)
    s = np.sin(a)
    return np.array([  [1,0,0,0],
                        [0,c,-s,0],
                        [0,s,c,0],
                        [0,0,0,1]])
def Ry4(a):
    a = np.radians(a)
    c = np.cos(a)
    s = np.sin(a)
    return np.array([[c,0,s,0],
                     [0,1,0,0],
                     [-s,0,c,0],
                     [0,0,0,1]])
                
def Rz4(a):
    a = np.radians(a)
    c = np.cos(a)
    s = np.sin(a)
    return np.array([[c,-s,0,0],
                     [s,c,0,0],
                     [0,0,1,0],
                     [0,0,0,1]])

def T4(tx,ty,tz):
    return np.array([[1,0,0,tx],
                     [0,1,0,ty],
                     [0,0,1,tz],
                     [0,0,0,1]])

def operaciones_respecto_fijo():
    rx_90_n = Rx4(-90)
    t_5510 = T4(5,5,10)
    rz_90 = Rz4(90)
    H = rz_90@t_5510@rx_90_n
    print(H)

def operaciones_respecto_movil():
    t_31010 = T4(-3,10,10)
    rx_90_n = Rx4(-90)
    ry_90   = Ry4(90)
    H = t_31010@rx_90_n@ry_90 
    print(H)

def ejercicio1():
    #a) fijo 
    rz_90 = Rz4(90)
    ry_90_n = Ry4(-90)
    t = T4(3,3,3)
    H = t @ ry_90_n @ rz_90
    print(H)
    print("\n")
    #b) moviles 
    rz_90 = Rz4(90)
    rx_90_n = Rx4(-90)
    t = T4(3,-3,-3)
    H = rz_90 @ rx_90_n @ t 
    print(H)

def ejercicio2():
    rz_90 = Rz4(90) ; t = T4(0,-3,2)
    H12 = rz_90 @ t
    rx_90_n = Rx4(-90) ; t = T4(3,-1,0)
    H23 = rx_90_n @ t
    H = H12 @ H23
    print(H)

def ejercicio3():
    #a)  en uvw es (0,2,1) 
    H12 = T4(3,0,2)@Rz4(90) # respecto al fijo 
    Xuvw = np.array([0,2,1,1])
    Xxyz = H12 @ Xuvw
    print(Xxyz)
    #b) Xx3y3z3 ? 
    H23 = Rx4(-90) @ T4(3,-1,0)
    #Xuvw = H23 @ Xx3y3z3
    Xx3x3z3 = np.linalg.inv(H23) @ Xuvw
    print(Xx3x3z3)


def ejercicio4():
    #Oxayaza → Oxcyczc   
    # primero traslacion lueego 2 rotaciones respecto a moviless revisar imagen en README
    H12 =  T4(3,0,2) @ Ry4(90) @ Rx4(-30)
    print(H12)

def ejercicio5():
    H12 = T4(3,0,0) @ Rz4(180) 
    #print(H12)
    H23 = T4(0,0,2) @ Ry4(90) @ Rx4(150)
    H = H12 @ H23
    print(H)

def ejercicio6():       #movil
    # = T4(0,3,2) @ Rx4(-90) @ Ry4(180)
    #Rz4(180-36.9)@Rx4(90)@T4(3,0,0)  fijo 
    #H = Rx4(-90)@T4(3,0,0)@T4(0,4,2) @ Rz4(-180) @ Rx4(-90)@Rz4(180-36.9)
    #todo movil 
    H = T4(0,4,2) @ Rx4(-90)@Ry4(180)@T4(3,0,0)@Rx4(-90)@Rz4(180-36.9)
    print(H)
    # vveer ejercicio 1 si es caso movil y la traslacion se hace al final

def ejercicio7():
        H01 = T4(0,1,1) @ Ry4(90) @ Rz4(90)
        H12 = T4(0.5,0.1,-0.5) @ Ry4(90) @ Rz4(90)
        H23 = T4(1.9,0,0) @ Ry4(-90)
        print(f"H01:\n  {H01}")
        print(f"H02:\n{H01@H12}")
        print(f"H03:\n{H01@H12@H23}")
        
def ejercicio8():
    H01 = T4(0,1,1) @ Ry4(90) @ Rz4(90)
    H12 = T4(0.5,0.1,-0.5) @ Ry4(90) @ Rz4(90)
    H23 = T4(1.9,0,0) @ Ry4(-90)
    #antiguo centro (0.5,0.1,-0.5) respecto x1y1z1 → (0.5,-0.5,'-0.1) respecto a rotado Rz4(90)
    #entonces hago 
    H12_prima = T4(0.5,0.8,0.1) @ H12 @ Rz4(90)
    H13 = T4(0.5,2,-0.5) @ Rx4(90)
    #H13 = H12_prima Hbloque_camara
    Hbloque_camara = np.linalg.inv(H12_prima)@H13
    print(f"H {Hbloque_camara}")
    H0bloque = H01 @ H12_prima

if __name__=='__main__':
    operaciones_respecto_fijo()
    print("\n")
    operaciones_respecto_movil()
    print("\n")
    ejercicio1()
    print("\n")
    ejercicio2()
    print("\n")
    ejercicio3()
    print("\n")
    ejercicio4()
    print("\n")
    ejercicio5()
    print("\n")
    ejercicio6()
    print("\n")
    ejercicio7()
    print("\n")
    ejercicio8()