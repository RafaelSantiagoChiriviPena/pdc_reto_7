import random       # se importa la libreria random para generar el numero
if __name__ == "__main__":
    try: 
        adiv : int = random.randint(1, 100)     # generar el numero y asignarlo a una variable
        intento : int = input("Por favor, trate de adivinar el numero generado por la maquina, este se encuentra entre 1 y 100: ")      # ingreso del valor para adivinar
        while str(intento) != str(adiv):    # ciclo hasta adivinar
            if str(intento) > str(adiv):    # caso adivinanza mayor que numero generado
                intento = int(input("El numero ingresado esta por encima del numero generado, por favor, intentelo de nuevo: "))
            if str(intento) < str(adiv):    # caso adivinanza mayor que numero generado
                intento = int(input("El numero ingresado esta por debajo del numero generado, por favor, intentelo de nuevo: "))
        print(f"Felicidades! has adivinado el numero generado, este era {adiv}")
    except ValueError:
        print("El valor ingresado no se trata de un numero entero")