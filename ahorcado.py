import random

palabras = ['cocodrilo', 'tarea', 'ahorcado', 'software', 'juego']

palabra_secreta = random.choice(palabras)
#print(palabra_secreta)

letras_correctas = ['_'] * len(palabra_secreta) # creo arreglo de ['_'] multiplicado por el numero de letras de la plabara secreta
#print(letras_adivinadas)

letras_incorrectas = []
vidas = 3 #intentos

band_juego = False

print("¡Juego Ahorcado!")
print("La palabra tiene ", len(palabra_secreta), " letras.")
print()

while not band_juego:
    print()   
    print("Palabra:", ' '.join(letras_correctas))
    
    # Muestra las letras erradas
    print("Letras incorrectas:", ', '.join(letras_incorrectas))
    print("Vidas:", vidas)
    
    letra = ''

    while True:
        letra = input("Dame una letra: ")

        if len(letra) != 1:
            print("Por favor, ingresa una letra.")
            continue
        
        # valida si la letra ya fue usada
        if letra in letras_correctas or letra in letras_incorrectas:
            print("Ya utilizaste esta letra. Intenta otra.")
            continue
        
        break
    
    if letra in palabra_secreta:
        print("¡Acertaste! La letra está en la palabra.")
        
        posicion = 0
        for auxLetra in palabra_secreta:
            if auxLetra == letra:
                letras_correctas[posicion] = letra
            posicion += 1
    else:
        print("Incorrecto. La letra no está en la palabra.")
        letras_incorrectas.append(letra)
        vidas -= 1

    if '_' not in letras_correctas:
        print()
        print("¡Ganaste!")
        print("La palabra es:", palabra_secreta)
        print()
        band_juego = True
    
    if vidas == 0:
        print()
        print("¡Perdiste!")
        print(f"La palabra secreta es: {palabra_secreta}")
        print()
        band_juego = True