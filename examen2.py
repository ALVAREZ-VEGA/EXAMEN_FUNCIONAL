# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:52:01 2020

  ******************** ALVAREZ VEGA SOCORRO *******************
EXAMEN INCISO 2.

Bada Boom!!! <generadores> 20 pts
	
	Defina un generador que reciba un numero entero positivo mayor a 0 N,
	dicho generador proporciona numero de 1 hasta N
	con las siguientes condiciones:
		1) si es multiplo de 3 coloque la cadena "Bada"
		2) si es multiplo de 5 coloque la cadena "Boom!!"
		3) si es multiplo de 3 y 5 coloque "Bada Boom!!"
		
	def genBadaBoom(N):
		pass
		
	a = genBadaBoom(10)
	z = [e for e in a]
	print(z)
	#[1,2,"Bada",4,"Boom","Bada",7,8,"Bada","Boom"]

@author: Kokiz
"""
def genBadaBoom(N):
    J = 1
    while J <= N :
        bada = J % 3 == 0
        boom = J % 5 == 0
        if bada and boom: # comprueba si el numero es divisible entre 3 y 5
            yield "BadaBoom!"
            J = J + 1
        elif bada: # comprueba si el numero es divisible entre 3 
            yield "Bada"
            J = J + 1
        elif boom: # comprueba si el numero es divisible entre 5
            yield "Boom"
            J = J + 1
        else:
            yield J
            J = J + 1
    
    
a = genBadaBoom(10)
z = [e for e in a]
print(z)
    
