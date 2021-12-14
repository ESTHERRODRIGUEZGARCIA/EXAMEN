from random import randint
import math
import os
import re
import sys
import chess

#Comienzo definiendo el tablero y la posición aleatoria de las piezas

tablero = [
    ['  ', '  ', '  '], 
    ['  ', '  ', '  '],
    ['  ', '  ', '  '], 
    ]

x = randint(0,2)
y = randint(0,2)
z = randint(0,2)
a = randint(0,2)
b = randint(0,2)
c = randint(0,2)

(tablero[x])[0] = "♜"
(tablero[y])[1] = "♜"
(tablero[z])[2] = "♜"
(tablero[a])[0] = "♖"
(tablero[b])[1] = "♖"
(tablero[c])[2] = "♖"

print(tablero)

while a == x:
    x = randint(0,2)
while b == y:
    y = randint(0,2)
while c == z:
    z = randint(0,2)

#SEGUNDA PARTE 

def encerrada(fila,columna):
    if fila == 0 and tablero[fila+1][columna] != " ":
        error = True
    elif fila ==1:
        if tablero[fila+1][columna] != " ":
            error = True
        else:
            error = False
    elif fila == 2 and tablero[fila-1][columna] != " ":
        error = True
    else:
        error = False
    return error

#ahora quiero mostrar el tablero:
def muestra_ajedrez(tablero):
    muestra = 0 #comienza de 0
    for tablero [muestra]in tablero:
        print(tablero[muestra])
        muestra += 1
    print("\n")

#MOVIMIENTOS
def movimiento(fila, columna):
    if fila == 0:
        tablero [fila+1][columna] = tablero[fila][columna]
        tablero[fila][columna] = " "
    elif fila ==1:
        if tablero[fila+1][columna] != "":
            tablero[fila-1][columna] = tablero[fila][columna]
            tablero[fila][columna] = " "
        else:
            tablero[fila+1][columna] =tablero[fila][columna] 
            tablero[fila][columna] = " "
    elif fila == 2:
        tablero[fila-1][columna] = tablero[fila][columna] 
        tablero[fila][columna] = " "

def cambio(fila, columna):
    if fila == 0:
        fila += 1
    elif fila == 1:
        if tablero[fila+1][columna] != " ":
            fila -= 1
        else:
            fila += 1
    elif fila == 2:
        fila -= 1
    return fila

while True:
    encerradax = encerrada(x,0)
    encerraday = encerrada(y,1)
    encerradaz = encerrada(z,2)
    encerradaa = encerrada(a,0)
    encerradab = encerrada(b,1)
    encerradac = encerrada(c,2)
    if encerradax == True and encerraday == True and encerradaz == True:
        print("El jugador 1 no puede mover. Nueva creación del tablero. ")
        pass
    elif encerradaa == True and encerradab == True and encerradac == True:
        print("El jugador 2 no puede mover. Nueva creación del tablero. ")
        pass
    else: 
        break
    
turno = randint(0,1)
while True:
    if turno ==1:
        if encerradax == False and encerradaa == False:

