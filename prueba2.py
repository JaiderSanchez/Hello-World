import random
import math
def suma_dos_valores(sumando1, sumando2):
    global resultado
    resultado = sumando1 + sumando2
    return resultado

# Invocando la función con dos valores 4 y 5
suma_dos_valores(4, 5)
print("primera suma")
print("El resultado de la  1er suma es: ", resultado)  # Imprime el resultado en la consola
suma_dos_valores(1,2)
print("segunda suma")
print("El resultado de la 2da suma es: ", resultado) # Imprime el resultado en la consola

def calculadora_dos_valores(numero1, numero2, operador):
    global resultado
    if operador == 1: # Si el operador es 1, es suma
        resultado = numero1 + numero2
        return resultado
    elif operador == 2: # Si el operador es 2, es resta
        resultado = numero1 - numero2
        return resultado 
    elif operador == 3: # Si el operador es 3, es multiplicación
        resultado = numero1 * numero2
        return resultado
    elif operador == 4: # Si el operador es 4, es división
        if numero2 == 0:
            return "Error: No se puede dividir por cero"
        else:
            resultado = numero1 / numero2
            return resultado
    else: # Si el operador es otro número
        print("El número ingresado no es válido")
    return resultado

calculadora_dos_valores(1, 2, 1)
print("Suma", resultado)
calculadora_dos_valores(1, 2, 2)
print("Resta", resultado)
calculadora_dos_valores(1, 2, 3)
print("Multiplicacion", resultado)
calculadora_dos_valores(1, 2, 4)
print("División", resultado)

# Ejercicio para calcular el teorema de pitágoras

def calculadora_teorema_pitágoras(a, b):
    global c
    a = 3
    b = 4
    c = (a ** 2 + b ** 2) ** 0.5
    return c

calculadora_teorema_pitágoras(3, 4)
print("c =", c)

# Ejercicio para 
def despeje_x():
    global x
    b = int(input("Ingrese el valor de B "))
    c = int(input("Ingrese el valor de C "))
    x = (c - b)/2
    print("El valor de x es: ", x)
    return x

despeje_x()

# Compuerta "and" de 3 entradas

def compuerta_and():
    global resultado
    A = bool(input("Ingrese el valor de A "))
    B = bool(input("Ingrese el valor de B "))
    C = bool(input("Ingrese el valor de C "))
    resultado = A and B and C
    print("El resultado de la tabla de verdad es : ", resultado)
    return resultado
        
compuerta_and()

def pitagoras_funcion_sumar():
    global resul_pitagoras
    a = int(input("Ingrese el valor de a = "))
    b = int(input("Ingrese el valor de b = "))
    a2 = a ** 2
    b2 = b ** 2
    suma = pitagoras_funcion_sumar(a2, b2)
    resul_pitagoras = suma ** 0.5
    print("El valor de pitágoras es: ", resul_pitagoras)
    return resul_pitagoras

pitagoras_funcion_sumar()

# Proyecto Zoologico
def contar_palabras():
    global resultado_contador
    Texto = str(input("Ingresa alguna oración "))
    Letra = str(input("ingresa la letra que quieres buscar: "))
    resultado_contador = Texto.count(Letra) 
    print("La cantidad de letras es ", resultado_contador)
    return resultado_contador
contar_palabras()

def contador_palabras():
     global resultado_contador
     Palabra = str(input("Ingresa alguna oración "))
     Letra = str(input("Ingresa la letra a contar: "))
     resultado_contador = Palabra.count(Letra)
     print("La cantidad de letras es ", Letra, "es: " , resultado_contador)
     print("La cantidad de letras de la palabra es: ", len(Palabra))
     print("Palabra separada por letras: ", list(Palabra))
     return resultado_contador
contador_palabras()

def juego_piedra_papel_tijera():
    import random
def eleccion(jugada):
    if jugada == 1:
        return "Piedra 🥌"
    elif jugada == 2:
        return "Papel 📰"
    elif jugada == 3:
        return "Tijeras ✂️"
    else:
        return "Elección incorrecta"

def juego_piedra_papel_tijera():
    jugador1 = random.randint(1, 3)  # 1 es piedra, 2 es papel, 3 es tijera
    jugador2 = random.randint(1, 3)

    print("Jugador 1 elige:", eleccion(jugador1))
    print("Jugador 2 elige:", eleccion(jugador2))

    # Combate entre jugador 1 y jugador 2
    if jugador1 == jugador2:
        print("Empate")
    elif (jugador1 == 1 and jugador2 == 3) or (jugador1 == 2 and jugador2 == 1) or (jugador1 == 3 and jugador2 == 2):
        print("Ganó el jugador 1")
    else:
        print("Ganó el jugador 2")

juego_piedra_papel_tijera()