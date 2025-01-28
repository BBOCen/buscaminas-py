import os
import random

# Ejercicio 3

# En este ejercicio el usuario puede moverse de arriba, abajo, izquierda o derecha

# Aquí se van a definir las funciones del programa

# Esta función imprime la "ubicación actual del usuario en el cuadrícula"
def imprimir_coordenada(cuadricula, y_usuario, x_usuario):

    # Ahora vamos a imprimir donde está el usuario
    print(f"La coordenada actual es: \ny: {y_usuario} x: {x_usuario}\n")

    # Para imprimir la X vamos a tener que sustituir el valor del array, para guardarlo usamos esta variable
    temp = 0

    for i in range(len(cuadricula)):
        if i == 0:
            array = []
            for j in range(len(cuadricula[i]) * 2 + 2):
                if j % 2 != 0:
                    array.append(" ")
                else:
                    array.append(j // 2)
            string_array = "   " + "".join(map(str, array))
            print(string_array)

        if i == y_usuario:
            temp = cuadricula[y_usuario][x_usuario]
            cuadricula[i][x_usuario] = "X"

        print(f"{i} {cuadricula[i]}")

    # Aquí reemplazamos el valor del elemento del array cuadricula del usuario con la variable temp
    cuadricula[y_usuario][x_usuario] = temp

# Esta función verifica si se ha encontrado el tesoro
def verificar_tesoro(y_usuario, x_usuario, y_tesoro, x_tesoro):
    if y_usuario == y_tesoro and x_usuario == x_tesoro:
        print("¡Has encontrado el tesoro!")
        return True
    else:
        print("El tesoro no está aquí")
        return False

# Esta función maneja la lógica de las decisiones del usuario relacionados con el movimiento sobre la cuadrícula
def realizar_movimiento(decision, y_usuario, x_usuario, cuadricula):
    # Subir
    if decision == "w":
        # La posición 0 es la única en la que al subir, se tiene que ir al último
        if y_usuario == 0:
            y_usuario = len(cuadricula) - 1
        else:
            y_usuario -= 1
    # Bajar
    elif decision == "s":
        if y_usuario == len(cuadricula) - 1:
            y_usuario = 0
        else:
            y_usuario += 1
    # Ir a la izquierda
    elif decision == "a":
        if x_usuario == 0:
            x_usuario = len(cuadricula[y_usuario]) - 1
        else:
            x_usuario -= 1
    # Ir a la derecha
    elif decision == "d":
        if x_usuario == len(cuadricula[y_usuario]) - 1:
            x_usuario = 0
        else:
            x_usuario += 1
    return y_usuario, x_usuario

def limpiar_consola():
    # Esto imprimirá muchas líneas en blanco para simular el "limpiar" la consola
    print("\n" * 50)  # Imprime 50 líneas en blanco

# Este array va a ser la cuadrícula
cuadricula = [
    [0, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5],
]

# La siguiente variable representa el punto del array en el que se encontrará el tesoro
# Esta variable generará el eje y del tesoro
y_tesoro = random.randint(0, len(cuadricula) - 1)

# Esta variable generará el eje x del tesoro
x_tesoro = random.choice(cuadricula[y_tesoro])

# Estas variables representan las coordenadas del usuario
# El usuario empieza en el punto 0,0
y_usuario, x_usuario = 0, 0

# Estas variables representan el valor máximo que pueden tener las coordenadas (la longitud del array - 1)
y_maximo = len(cuadricula) - 1
x_maximo = len(cuadricula[0]) - 1

# Esta variable controla la ejecución del bucle while
salir = False

# Esta variable es la decisión del usuario
decision = ""

# Bucle principal
while not salir:
    # Vamos a preguntarle la decisión del usuario
    imprimir_coordenada(cuadricula, y_usuario, x_usuario)
    decision = input(
        "\n¿Qué quieres hacer (abre la consola para ver el juego)? \n1. Subir (introduce W) \n2. Bajar (introduce S) \n3. Ir a la izquierda (introduce A) \n4. Ir a la derecha (introduce D) \n5. Excavar (introduce E) \n6. Salir del programa (introduce 0) \nLos controles serían: \n  W \nA S D: "
    ).lower()

    # Este if comprueba si el usuario quiere realizar algún movimiento
    if decision in ["w", "a", "s", "d"]:
        y_usuario, x_usuario = realizar_movimiento(decision, y_usuario, x_usuario, cuadricula)

    # Excavar el tesoro
    elif decision == "e":
        encontrado = verificar_tesoro(y_usuario, x_usuario, y_tesoro, x_tesoro)
        if encontrado:
            salir = True
            continue

    # Salir
    elif decision == "0":
        print("Has salido del programa")
        salir = True
        continue

    # Esta es una opción "secreta" de desarrollo, al pulsar "m" se mostrará las coordenadas del tesoro hasta que el usuario pulse salir
    elif decision == "m":
        entrada = ""
        while entrada != "salir":
            print(f"El tesoro está en las siguientes coordenadas: y: {y_tesoro} x: {x_tesoro}")
            entrada = input("Se ha mostrado en la consola las coordenadas del tesoro, teclea \"salir\" para seguir con el juego").lower()
    # Esto avisa al usuario si ha introducido una opción inválida
    else:
        print("Parámetros incorrectos, introduce una opción válida")

    # Limpiamos la consola para que se vea todo claramente (como no se puede borrar todo el contenido naterior, se imprimen 50 líneas en blanco)
    limpiar_consola()
