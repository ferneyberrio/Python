# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 06:13:58 2021

@author: Ferney
"""

print("*********************************************")
print("Principios magneticos Quiz Problema Tipo 2" )
print("*********************************************\n")

import math   # importar libreria para operaciones matematicas
#import cmath  # importar libreria para operaciones matematicas con complejos
PI = math.pi             # nombrar com PI el valor de pi



# Archivo  para Quiz circuitos magneticos

prof = 100 / 10                           # profundidad en cm

L1 =  15/100                       # Longitud de la región 1  (metros)
L2 = 10/100                        # Longitud de la región 2  (metros)
L3 = 30/100                        # Longitud de la región 3  (metros)
L4 =  15/100                       # Longitud de la región 4  (metros)
L5 = 30/100                        # Longitud de la región 5  (metros)
L6 = 30/100                        # Longitud de la región 6  (metros)

LA = (L1/2) + (L5) + (L6/2)        # longitud Reluctancia1
LB = (L4/2) + (L3) + (L2/2)        # longitud Reluctancia2
LC = (L1/2) + (L5) + (L6/2)        # longitud Reluctancia3
LD = (L4/2) + (L3) + (L2/2)        # longitud Reluctancia4


A1 = L4*prof*100/10000                    # Área de la región 1 (metros) / equivalencia en m^2
A2 = L1*prof*100/10000                    # Área de la región 2  (metros)
A3 = L2*prof*100/10000                    # Área de la región 3 (metros) / equivalencia en m^2
A4 = L6*prof*100/10000                    # Área de la región 4 (metros) / equivalencia en m^2


ur = 2500                        # Permeabilidad relativa
u0 = 4*PI*1e-7                   # Permeabilidad del espacio libre
u = ur *  u0                     # permeabilidad del material

n = 200                          # Número de vueltas sobre el núcleo

flujo = 0.0048


print("Calculos Automáticos : \n" )


# Calcular la primera reluctancia

R1 =  LA / (u * A1)               # calculo reluctancia 1
print ("Reluctancia 1 =  ", R1, "A-vuelta/Wb")      # mostrar Reluctancia

# Calcular la segunda reluctancia

R2 = LB / (u * A2);
print ("Reluctancia 2 =  ", R2, "A-vuelta/Wb")   # mostrar Reluctancia

# Calcular la tercera reluctancia

R3 =  LC / (u * A3)               # calculo reluctancia 1
print ("Reluctancia 3 =  ", R3, "A-vuelta/Wb")   # mostrar Reluctancia

# Calcular la cuarta reluctancia

R4 = LD / (u * A4);
print ("Reluctancia 4 =  ", R4, "A-vuelta/Wb \n")   # mostrar Reluctancia



# Calcular la reluctancia total
Rtot = R1 + R2 + R3 + R4

F = flujo * Rtot                    # fuerza magnetomotriz

i = F / n                           # corriente
print ("Corriente =  ", i, "A \n")

# densidades de campo magnético
B1 = flujo/A1
print ("Densidad =  ", B1, "T")
B2 = flujo/A2
print ("Densidad 2 =  ", B2, "T")
B3 = flujo/A3
print ("Densidad 3 =  ", B3, "T")
B4 = flujo/A4
print ("Densidad 4 =  ", B4, "T")

#H1 = n / LA
#H2 = n / LB
#H3 = n / LC
#H4 = n / LD


