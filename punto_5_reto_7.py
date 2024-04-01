fact : int = 1      #constante 
numero : int = 1    #constante
if __name__ == "__main__":
    try:
        n : int = int(input("Ingrese un numero entero positivo al que obtener el factorial: ")) #ingreso de numero para aplicar operacion
        while n < 0:
            n = int(input("El numero ingresado no se trataba de un entero positivo, por favor intentelo de nuevo: "))
        while n > 1: #limite de regresion
            fact = fact * n #operacion de factorial
            n -= 1 #regresion hasta 1
            numero += 1
        if n == 0: #caso especial 0!
            fact = 1
            numero = 0
        print(f"el factorial del numero ingresado {numero} es {fact}")
    except ValueError:
        print("El numero ingresado no se trata de un numero entero")