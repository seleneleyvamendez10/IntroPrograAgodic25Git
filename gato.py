import random

# Creamos gato
arregloGato = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

# Sirve para mostrar posiciones al usuario
gato = """
  {0} | {1} | {2}
 ---+---+---
  {3} | {4} | {5}
 ---+---+---
  {6} | {7} | {8}
"""

jugador= "X"
band_juego = True
ganador = None
turno = 0

tipoDeJuego = ""

print("Gato")
tipoDeJuego = input("Seleccione tipo de juego (1: J vs J, 2: J vs CPU): ")

# ¡Comenzamos!
while band_juego:

    valGato = arregloGato[0] + arregloGato[1] + arregloGato[2]
    print(gato.format(*valGato))
    print(f"Jugador {jugador}:")
    
    posicionGato = False
    posicion = -1
    
    if tipoDeJuego == "2" and jugador == "O": 
        print("Jugador CPU...")
        vacias = []
        for i in range(3):
            for j in range(3):
                if arregloGato[i][j] not in ["X", "O"]:
                    # Guardamos la posición (1-9) para que choice la use
                    vacias.append(int(arregloGato[i][j]))
        
        if vacias:
            posicion = random.choice(vacias)
            print(f"Posición CPU: **{posicion}**")
            posicionGato = True
            
    else: # Turno del Jugador 1 o 2
        while not posicionGato:
            try:
                entrada = input("Elige una posición (1-9): ")
                posicion = int(entrada)
                if 1 <= posicion <= 9:
                
                    fila = (posicion - 1) // 3
                    columna = (posicion - 1) % 3
                    
                    if arregloGato[fila][columna] not in ["X", "O"]:
                        posicionGato = True
                    else:
                        print("Posición ocupada. Intenta de nuevo.")
                else:
                    print("Ingresa un número entre 1 y 9.")
            except ValueError:
                print("Entrada no válida. Ingresa solo el número.")


    if posicionGato:
        fila = (posicion - 1) // 3
        columna = (posicion - 1) % 3
        arregloGato[fila][columna] = jugador
        turno += 1

        linGanadoras = [
            (arregloGato[0][0], arregloGato[0][1], arregloGato[0][2]), # H1
            (arregloGato[1][0], arregloGato[1][1], arregloGato[1][2]), # H2
            (arregloGato[2][0], arregloGato[2][1], arregloGato[2][2]), # H3
            (arregloGato[0][0], arregloGato[1][0], arregloGato[2][0]), # V1
            (arregloGato[0][1], arregloGato[1][1], arregloGato[2][1]), # V2
            (arregloGato[0][2], arregloGato[1][2], arregloGato[2][2]), # V3
            (arregloGato[0][0], arregloGato[1][1], arregloGato[2][2]), # D1
            (arregloGato[0][2], arregloGato[1][1], arregloGato[2][0])  # D2
        ]
        
        for linea in linGanadoras:
            if linea[0] == linea[1] and linea[1] == linea[2]:
                ganador = jugador
                band_juego = False
                break

        # Empate
        if turno == 9 and not ganador:
            band_juego = False
            
        # 6. Cambiar de jugador y continua el juego
        if band_juego:
            if jugador == "X":
                jugador = "O"
            else:
                jugador = "X"

#Juego terminado
print("Juego Terminado")
valGato = arregloGato[0] + arregloGato[1] + arregloGato[2]
print(gato.format(*valGato)) # Mostrar gato final

if ganador:
    print(f"¡{ganador} ganaste!")
else:
    print("¡Empate!")

