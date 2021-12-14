#juego banana
import random
def jugador1():
    print("Nombre de jugador 1")
    global jugador1
    jugador1= str(input())
    listajugador1 = []
    global puntuacion1
    

    for i in range(2):
        letra = random.randint()
        listajugador1.append(letra)
    valor1=listajugador1[0]
    valor2=listajugador1[1]
    if valor1 == valor2:
        print(listajugador1)
        puntuacion1 = valor1
        print(f"La puntuacion de {jugador1} es {puntuacion1}")
    else:
        n = 0
        while valor1 != valor2:
            n += 1
            letra = random.randint()
            listajugador1.append(letra)
            valor1=listajugador1[n]
            valor2=listajugador1[n +1]
            print(listajugador1)
            if valor1 == valor2:
                puntuacion1 = valor1
                print(f"La puntuacion de {jugador1} es {puntuacion1}")
jugador1()

def jugador2():
    print("Nombre de jugador 2")
    global jugador2
    jugador2= str(input())
    listajugador2 = []
    global puntuacion2
    
    for i in range():
        letra = random.randint()
        listajugador2.append(letra)
    valor1=listajugador2[0]
    valor2=listajugador2[1]
    if valor1 == valor2:
        print(listajugador2)
        puntuacion2 = valor1
        print(f"La puntuacion de {jugador2} es {puntuacion2}")
    else:
        n = 0
        while valor1 != valor2:
            n += 1
            letra = random.randint()
            listajugador2.append(letra)
            valor1=listajugador2[n]
            valor2=listajugador2[n +1]
            print(listajugador2)
            if valor1 == valor2:
                puntuacion2 = valor1
                print(f"La puntuacion de {jugador2} es {puntuacion2}")
jugador2()