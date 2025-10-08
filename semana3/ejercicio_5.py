import numpy as np  
#• Rotar el vector [2,3,4] usando ángulos de Euler en la convención WVW.
#Los ángulos que utilizaremos serán:
#- Primero, una rotación de 45o alrededor del eje Z.
#- Luego, una rotación de 30o alrededor del eje V’.
#1- Finalmente, otra rotación de −60o alrededor del eje W''.

v = np.array([2,3,4])

R = Rz(45) @ Rx(30) @ Rz(-60)
v_final = R @ v
#phi = 45, theta y ota vezphi

    