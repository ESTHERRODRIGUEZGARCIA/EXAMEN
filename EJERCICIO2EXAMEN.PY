from random import randint
import math
import os
import re
import sys
import chess

#Comienzo definiendo el tablero y la posición aleatoria de las piezas
board=('♜\t♜\t♜\t') 
#tupla pues este tablero es siempre el mismo
print(board)

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


while a == x:
    x = randint(0,2)
while b == y:
    y = randint(0,2)
while c == z:
    z = randint(0,2)

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

    