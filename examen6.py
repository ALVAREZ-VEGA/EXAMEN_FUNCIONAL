# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:59:54 2020

****************** ALVAREZ VEGA SOCORRO ***************

EXMEN INCISO 6.

<Monads>

--Hole in my soul apocalyptica--  20 pts

There's a hole in my heart, in my life, in my way
And it's filled with regret and all I did, to push you away
If there's still a place in your life, in your heart for me
I would do anything, so don't ask me to leave

I've got a hole in my soul where you use to be
You're the thorn in my heart and you're killing me
I wish I could go back and do it all differently
I wish that I'd treated you differently
'Cause now there's a hole in my soul where you use to be

El fragmento anterior es un canción del grupo apocalyptica

Usando Monads obtenga la letra 
que menos se repite de todo el fragmento y obtenga la probabilidad de sacar dicha
letra.


@author: Kokiz
"""
FRAGMENTO = ["""There's a hole in my heart, in my life, in my
     way And it's filled with regret and all I did, to push you away
    If there's still a place in your life, in your heart for me
    I would do anything, so don't ask me to leave
    I've got a hole in my soul where you use to be
    You're the thorn in my heart and you're killing me
    I wish I could go back and do it all differently
    I wish that I'd treated you differently
    'Cause now there's a hole in my soul where you use to be"""]

################################################################
from functools import reduce
def numero_apariciones(elemento,L):
    total = 0
    for i in L:
        if elemento == i:
            total += 1
    return total + 1

################################################################
def funcion(L):
    C = []
    N = []
    CONT = []
    
    if not L:
        return []
    primero = L[0]
    for i in primero:
        if not i in C:
            if i != ' ':
                if i != '\n':
                    C.append(i)
        else:
            N.append(i)
    for a in C:
        CONT.append(numero_apariciones(a, N))
    P = reduce(lambda a,b: a + b, CONT)
    print('probabilidad de sacar dicha letra: 1 /',P)
    print(' ')
    total_letras = list(zip(C, CONT))
    return total_letras


############################################################
A = funcion(FRAGMENTO)
B = filter(lambda a: a[1] == 1, A)
D = list(B)
R = map(lambda e: e[0],D)
H = list(R)
print('Letras que menos aparecen en el fragmento : ',H)


