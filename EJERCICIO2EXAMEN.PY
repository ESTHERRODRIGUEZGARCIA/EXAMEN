from random import randint
import math
import os
import re
import sys

tablero = [
    ['  ', '  ', '  '], 
    ['  ', '  ', '  '],
    ['  ', '  ', '  '], 
   ]

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

    