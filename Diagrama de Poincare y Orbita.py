"""
Resolucion de la ecuacion diferencial de Van der Pol.
Condiciones: sin termino oscilante, e = 1.0, x = 0.0, v = 1.0, N = 1000, t = 100.
Grafico: Espacio de fases
"""

from pylab import *
from matplotlib import *
from scipy.integrate import odeint

N = 1000 #Pasos en Tiempo

"""
Una ecuacion, dos variable de estado, la posicion x y la velocidad v
"""

estado = zeros([2])

x = 0.0         #Posicion inicial del oscilador
v = 1.0         #Velocidad inicial del oscilador

estado[0] = x        #Estado inicial del sistema
estado[1] = v

tiempo = linspace(0, 100, N)

e = 1.0

def van_der_pol_sinosc(estado, tiempo):
    """
    ecuacion diferencial del oscilador de van der pol sin termino oscilante
    """
    g0 = estado[1]
    g1 = e*(1-estado[0]*estado[0])*estado[1]-estado[0]

    return array([g0, g1])

#Solucion para la ecuacion
calculo_vdp = odeint(van_der_pol_sinosc, estado, tiempo)
calculo_vdp_m = calculo_vdp[150: ]      #Se eliminan los efectos iniciales

#Seccion para el diagrama de poincare

P_x = []
P_v = []

for j in range(100,1000,100):   #Se toman puntos cada 10 segundos
    P_x.append(calculo_vdp[j,0])
    P_v.append(calculo_vdp[j,1])

#Grafico de la orbita y el diagrama de poincare de esta solucion.

plot(calculo_vdp_m[: ,0], calculo_vdp_m[: ,1], 'k-')
plot(P_x, P_v, 'r.')
xlabel('Posicion')
ylabel('Velocidad')
suptitle('Espacio de Fases. Diagrama de Poincare y Orbita .\n Oscilador Van der Pol', fontsize=12, fontweight='bold')
title('e = 1.0, x_o = 0.0, v_o = 1.0, t = 100', fontsize=9)
show()
