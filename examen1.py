# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:42:49 2020

 ******************** ALVAREZ VEGA SOCORRO *******************
 
  EXAMEN INCISO  1.
  
   Primos  <generadores>  30 pts

	Realice una generador que devuelva  de todos lo numeros primos
	existentes de 0 hasta n-1 que cumpla con el siguiente prototipo:
	
	def gprimo(N):
		pass
	
	
	a = gprimo(10)
	z = [e for e in a]
	print(z)
	# [2, 3 ,5 ,7 ]
    
@author: Kokiz
"""
def gprimo(N):
# Funcion para calcular si es primo o no
    def num_primo(J):
        if J <= 1:
            return False
        for i in range(2,J):
            if J % i == 0:
                return False
        return True
    J = 0
    while J <= N:
        if num_primo(J):
            yield J 
        J = J + 1
        
    

a = gprimo(10)
z = [e for e in a]
print(z)
   