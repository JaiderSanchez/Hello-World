import time

def ejercicio_1 ():
    palabra= str(input("ingresar palabra: "))
    cantidad= int(input("ingrese la cantidad de veces: "))
    for i in range(cantidad):
        print("valor de la variable i: ", i + 1)
        print(palabra)
        time.sleep(1)
    return palabra


def ejercicio_edad ():
    edad= int(input("ingrese su edad: "))
    for i in range(edad):
        print("edad : ", i+1)
        print(i+1)
        time.sleep(1)

def ejercicio_calcular_edad ():
    año_actual= int(input("Ingrese el año actual: "))
    año_nacimiento= int(input("Ingrese el año nacimiento: "))
    edad= año_actual - año_nacimiento
    print("su edad es: ", edad)
    for i in range(edad):
        print(i+1)
        time.sleep(1)
    return edad


def numeros_impares ():
    numero= int(input("Ingrese el numero: "))

    for i in range(1, numero+1, 2):
        print (i, end="\n")
        time.sleep(1)
        if i==15:
            break;


numeros_impares()

def reloj_segundos():

    segundos= 60
    cantidad_seg= int(input("Ingrese el limite de segundos: "))
    for i in range(1, segundos + 1):
        print(i,"seg", end="\n")
        if i== cantidad_seg:
            break;
    print("\33[43m"+"Tiempo terminado"+"\33[0m")


def interes_anual():
    pesos_año= float(input("Cuanto dinero al año: "))
    tasa_interes= float(input("Tasa de interés anual: "))
    cantidad_años= int(input("Cuantos años: "))
    for i in range(1, cantidad_años+1):
        interes= pesos_año * (tasa_interes/100)
        pesos_año= pesos_año + interes
        print(f"En el año {i}, el dinero acumulado es: ${pesos_año:.2f}")
        time.sleep(1)

interes_anual()

def figura_asteriscos():
    global numero_asteriscos
    numero_asteriscos= int(input("Ingresa la cantidad de asteriscos: "))
    figura = ""
    for i in range(1, numero_asteriscos + 1):
        figura += "*" * i + "\n"
    return figura

print(figura_asteriscos())

def ciclo_edad():
    veces = 0
    print("¿Cuántos años tienes?")
    edad = int(input())
    while veces <= edad:
        veces += 1
        print(veces)
    
ciclo_edad()

def contador_reloj():
    segundos2= 60
    cantidad_segundos= int(input("Ingresa la cantidad de segundos"))
    for i in range(1, segundos2 + 1): # Cuenta hasta el tiempo máximo
        print(i, end="/n")
        # time.sleep(1)  # Esta función es para pausar el ejercicio por el segundo escrito dentro dentro del paréntesis, está comentado para que el ejercicio termine rápido.
        if i == cantidad_segundos:
            break;
        print("Juego terminado como en Halo 2")

contador_reloj()