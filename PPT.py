#libreria para numero aleatorio
import random

while True:
    #menu del juego
    print("Bienvenido/a al juego piedra, papel o tijera \n" \
    "Seleccione una de las siguientes opciones\n" \
    "1.- Piedra\n" \
    "2.- Papel\n" \
    "3.- Tijera\n" \
    "4.- Salir del juego")

    #variable jugador
    valor = int(input("Ingrese el numero: "))
    #para salir del juego
    if valor == 4:
        print("Gracias por jugar !!!")
        break
    #variable PC
    valorPc = random.randint(1,3)
    
    print("El jugador elige: %d\n"
    "El PC elige: %d"%(valor,valorPc))

    #Validaciones
    if (valor == valorPc):
        print("Es un empate")
    elif (valor ==1 and valorPc == 3) or (valor ==2 and valorPc == 1) or (valor ==3 and valorPc == 2):
        print("Ganaste")
    else:
        print("Perdiste")

