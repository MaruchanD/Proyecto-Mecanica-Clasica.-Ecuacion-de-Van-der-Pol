"""
Resolucion de la ecuacion diferencial de Van der Pol.
Condiciones: sin termino oscilante, e = 1.0, x = 1.0, v = 0.0, t = 100 .
Grafico: Espacio de fases
"""

from pylab import *
from matplotlib import *
from scipy.integrate import odeint

N=1000 #Pasos en Tiempo

"""
Una ecuacion, dos variable de estado, la posicion x y la velocidad v
"""

estado = zeros([2])

x = 1.0         #Posicion inicial del oscilador
v = 0.0         #Velocidad inicial del oscilador

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

#Grafico del espacio fase de esta solucion.

plot(calculo_vdp[: ,0], calculo_vdp[: ,1], 'k-')
xlabel('Posicion')
ylabel('Velocidad')
suptitle('Espacio de Fases. Oscilador Van der Pol', fontsize=12, fontweight='bold')
title('e = 1.0, x_o = 1.0, v_o = 0.0, t = 100', fontsize=9)
show()
