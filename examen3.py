# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:52:10 2020

     ******************** ALVAREZ VEGA SOCORRO *******************

 EXAMEN INCISO 3.
 
 Combinaciones <Comprensión de listas> 30pts
 Una tienda de ropa quiere saber cuantos conjuntos se pueden crear 
	a partir de un grupo de 5 camisas (roja,negra,azul,morada y cafe),      
	4 pantalones (negro, azul, cafe obscuro y crema) y uno de 4 accesorios
	posibles (cinturon, tirantes, lentes, fedora)
	
	1) Obtenga una lista con todos los conjuntos posibles e imprimala en pantalla
	2) imprima un mensaje donde mencione la cantidad de conjuntos posibles

@author: Kokiz
"""

CAMISAS = ['roja','negra','azul','morada','cafe']
PANTALONES = ['negro','azul','cafe obscuro','crema']
ACCESORIOS = ['cinturon','tirantes','lentes','fedora']

COMBINACIONES = [[a,b,c] for a in CAMISAS for b in PANTALONES for c in ACCESORIOS]
print (COMBINACIONES)
print (" ")
print ("El número de combinaciones posibles es: ",len(COMBINACIONES))

