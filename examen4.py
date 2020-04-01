# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:14:33 2020

 ******************** ALVAREZ VEGA SOCORRO ***************
 EXAMEN INCISO 4.

¿Fedora?  <Comprensión de listas >  15 pts

	Del problema anterior imprima una lista que tenga todos los conjuntos
	que incluyen un sombrero fedora y tambien despliegue su longitud
	
	

@author: Kokiz
"""

CAMISAS = ['roja','negra','azul','morada','cafe']
PANTALONES = ['negro','azul','cafe obscuro','crema']
ACCESORIOS = ['cinturon','tirantes','lentes','fedora']

COMBINACIONES = [[a,b,c] for a in CAMISAS for b in PANTALONES for c in ACCESORIOS]
FEDORA = [i for i in COMBINACIONES if i[2] == 'fedora']
print (FEDORA)
print (" ")
print ("El número de combinaciones posibles es: ",len(FEDORA))


