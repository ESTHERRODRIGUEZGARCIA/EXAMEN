# EXAMEN ESTHER ROFRÍGUEZ GARCÍA
Mi dirección de github es la siguiente:

https://github.com/ESTHERRODRIGUEZGARCIA/EXAMEN.git

# EJERCICIO 1 THE MINION GAME

# EJERCICIO 2
````
from random import randint
from sys import breakpointhook

import chess

#Comienzo definiendo el tablero y la posición aleatoria de las piezas


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

while a == x:
    x = randint(0,2)
while b == y:
    y = randint(0,2)
while c == z:
    z = randint(0,2)

(tablero[x])[0] = "♜"
(tablero[y])[1] = "♜"
(tablero[z])[2] = "♜"
(tablero[a])[0] = "♖"
(tablero[b])[1] = "♖"
(tablero[c])[2] = "♖"

muestra_ajedrez(tablero)

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
    breakpointhook
    
turno = randint(0,1)

while True:
    if turno ==1:
        if encerradax == False and encerradaa == False:
            movimiento(x,0)
            x = cambio(x,0)
            encerradaa = encerrada(a,0)
        elif encerraday == False and encerradab == False:
            movimiento(y,1)
            y = cambio(y,1)
            encerradab = encerrada(b,1)
        elif encerradaz == False and encerradac == False:
            movimiento(z,2)
            z = cambio(z,2)
            encerradac = encerrada(c,2)
        elif encerradaa == False:
            movimiento(a, 0)
            a = cambio(a, 0)
            encerradax = encerrada(x, 0)
        elif encerradab == False:
            movimiento(b, 1)
            b = cambio(b, 1)
            encerraday = encerrada(y, 1)
        elif encerradac == False:
            movimiento(c, 2)
            c = cambio(c, 2)
            encerradac = encerrada(z, 2)
        else:
            break
        turno = 1
    muestra_ajedrez(tablero)


muestra_ajedrez(tablero)
if encerradax == True and encerraday == True and encerradaz == True:
    print("El jugador 1 no se puede mover, ha ganado el jugador 2")
elif encerradaa == True and encerradab == True and encerradac == True:
    print("El jugador 2 no se puede mover, ha ganado el jugador 1")

````

````
#juego banana

import random
import string
random.choice(string.ascii_letters)



ascii_letters = ("A", "B", "N")

def jugador1():
    print("Introduce el nombre del jugador 1: ")
    global jugador1
    jugador1= str(input())
    lista_1 = []
    global puntuacion1
    

    for i in range(2):
        letra = random.choice(string.ascii_letters)
        lista_1.append(letra)
    valor1=lista_1[0]
    valor2=lista_1[1]
    if valor1 == valor2:
        print(lista_1)
        puntuacion1 = valor1
        print(f"La puntuacion de {jugador1} es {puntuacion1}")
    else:
        n = 0
        while valor1 != valor2:
            n += 1
            letra = random.choice(string.ascii_letters)
            lista_1.append(letra)
            valor1=lista_1[n]
            valor2=lista_1[n +1]
            print(lista_1)
            if valor1 == valor2:
                puntuacion1 = valor1
                print(f"La puntuacion de {jugador1} es {puntuacion1}")
jugador1()

def jugador2():
    print("Introduce el nombre del jugador 2: ")
    global jugador2
    jugador2= str(input())
    lista_2 = []
    global puntuacion2
    
    for i in range(2):
        letra = random.choice(string.ascii_letters)
        lista_2.append(letra)
    valor1=lista_2[0]
    valor2=lista_2[1]
    if valor1 == valor2:
        print(lista_2)
        puntuacion2 = valor1
        print(f"La puntuacion de {jugador2} es {puntuacion2}")
    else:
        n = 0
        while valor1 != valor2:
            n += 1
            letra = random.choice(string.ascii_letters)
            lista_2.append(letra)
            valor1=lista_2[n]
            valor2=lista_2[n +1]
            print(lista_2)
            if valor1 == valor2:
                puntuacion2 = valor1
                print(f"La puntuacion de {jugador2} es {puntuacion2}")
jugador2()

def ganador():
    if puntuacion1 > puntuacion2:
        print(f"Ha ganado {jugador1}")
    elif puntuacion1 < puntuacion2:
        print(f"Ha ganado {jugador2}")
    else:
        print("Empate")
ganador()

´´´´
