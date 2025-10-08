## Clase 05 Cuaternios
Un cuertenio una representación matemática que describe una rotación <br>

Constituido por 4 componentes q0,q1,q2,q3 que representan las coordenadas del cuaternio en una base {e,i,j,k}<br>
- "e : q0" es la parte escalar
- y el resto es la parte vectorial

```bash
 Q = [q0,q1,q2,q3]  = [s,V]
```
### Interpretacion del Cuaternio
sea ``Q = q0 + q1 i + q2 j + q3 k``<br>
Si se quiere representar una ROTACIÓN theta en radianes ALREDEDOR de un eje (kx,kj,kz) unitario los componentes del cuaternio se calcularían :<br>
- q0 = cos(theta/2)
- q1 = kx sin(theta/2) 
- q2 = kj sin(theta/2)
- q3 = kz sin(theta/2)

### Cuaternio Conjugado 
A un cuaternio se le puede asociar su conjugado ,cambiando el signo a la parte vectorial<br>
Q* = [q0, -q1, .q2, q3]  = [s,-v]
- (Q*)* = Q
- (Q1 ° Q2 )*  = Q1* ° Q2*
- Q* = Q^-1

### Operaciones algebraicas con cuaternios
Q1 ° Q2  = (s1,v1) ° (s2,v2)


