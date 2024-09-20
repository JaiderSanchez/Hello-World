def descubrir_contraseña():
    contraseña = "123456789"
    contraseña_ingresada = ""
    intento_ingresado = int(input("Por favor ingrese un número de intentos: "))
    intento = 0
    while intento < intento_ingresado:
        contraseña_ingresada = str(input("Ingresa una contraseña: "))
        if  contraseña_ingresada == contraseña:
            print("La contraseña es correcta")
            break
        else:
            print("La contraseña no coincide")
        intento += 1    
        # if contraseña_ingresada == contraseña:
        #     print("Contraseña correcta")
        #     break
        if  intento == intento_ingresado:
            print("Se llegó al límite de los intentos")
            break

descubrir_contraseña()

# Ejercicio de ingresar frase y buscar una letra por ingreso de usuario

def carácteres_palabra():
    frase = str(input("Ingrese la frase: "))
    letra = str(input("Ingrese la letra a buscar: "))
    contador = 0
    for i in frase:

        if i == letra:
            contador=contador+1
    print("La letra",letra,"se repite",contador,"veces")
              
carácteres_palabra()