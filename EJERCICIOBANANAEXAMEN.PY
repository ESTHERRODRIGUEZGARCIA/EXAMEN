#juego banana
import random
def player1():
    print("Nombre de jugador 1")
    global jugador1
    jugador1= str(input())
    listajugador1 = []
    global puntuacion1
    for i in range(2):
        num = random.randint(1,6)
        listajugador1.append(num)
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
            num = random.randint(1,6)
            listajugador1.append(num)
            valor1=listajugador1[n]
            valor2=listajugador1[n +1]
            print(listajugador1)
            if valor1 == valor2:
                puntuacion1 = valor1
                print(f"La puntuacion de {jugador1} es {puntuacion1}")
player1()