#juego banana
from random import randint
def jugador1():
    print("Introduce el nombre del jugador 1: ")
    global jugador1
    jugador1= str(input())
    lista_1 = []
    global puntuacion1
    

    for i in range(2):
        letra = randint()
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
            letra = randint()
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
    
    for i in range():
        letra = randint()
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
            letra = randint()
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