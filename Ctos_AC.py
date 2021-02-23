# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:27:45 2021

@author: Ferney
"""

import math     # importa libreria matematica
import cmath     # importa libreria matematica complejos
PI = cmath.pi


print("*********************************************")
print("Repaso Análisis circuitos AC . ejercicio 1" )
print("*********************************************\n")


# funcion para conocer el angulo de un numero complejo
def mi_angle( complejo ):    # funcion(numero a evaluar)   
	angulo=cmath.phase(complejo)*(180/PI)
	return angulo

# funcion para calcular la impedancia de un capacitor
def impedancia_capacitor(Vlr_capacitor):
    capacitor = (1/(W*Vlr_capacitor))*-1j	
    return capacitor

# funcion para calcular la impedancia de una bobina
def impedancia_bobina(Vlr_bobina):
     bobina = W*Vlr_bobina*1j
     return bobina
 
 # funcion para operar el prefijo de un elemento
def prefijo(numero,prefi):
    
    # exa=e18, peta=e15, tera=e12, giga=e9, mega=e6,kilo=e3, hecto=e2, deca=e1   
    # 1=e0
    # deci=e-1, centi=e-2, mili=e-3, micro=e-6, nano=e-9, pico=e-12
    
    if( prefi == "exa" ):
        return numero*1000000000000000000
    elif( prefi == "peta" ):
        return numero*1000000000000000
    elif( prefi == "tera" ):
        return numero*1000000000000
    elif( prefi == "giga" ):
        return numero*1000000000
    elif( prefi == "mega" ):
        return numero*1000000
    elif( prefi == "kilo" ):
        return numero*1000
    elif( prefi == "hecto" ):
        return numero*100
    elif( prefi == "deca" ):
        return numero*10
    elif( prefi == "cero" ):
        return numero*1
    elif( prefi == "deci" ):
        return numero/10
    elif( prefi == "centi" ):
        return numero/100
    elif( prefi == "mili" ):
        return numero/1000
    elif( prefi == "micro" ):
        return numero/1000000
    elif( prefi == "nano-9" ):
        return numero/1000000000
    elif( prefi == "pico" ):
        return numero/1000000000000
    else:
        print( "******************************************")
        print( "valor no valido en el prefijo del elemento")
   
vm=750
anguloVm=30
vs=cmath.rect(vm,anguloVm*(PI/180))
R=90
W=5000
L=prefijo( 32,"mili" ) 
C=prefijo( 5,"micro" )            

Xc=impedancia_capacitor(C)
Xl=impedancia_bobina(L)


Zt= R + Xc + Xl
it=vm/Zt
Is= (vs/Zt)

print("Xl = ",  Xl)
print("Xc = ", Xc)
print("Zt = ", Zt)
print("Z = ", abs(Zt),"¬",mi_angle(Zt),"°" )
print("it = ", it)
print("corriente = ", abs(it),"¬",mi_angle(it),"°\n")
print("is = ",  abs(Is),"cos(",W,"t",mi_angle(Is),"° )")

print()
