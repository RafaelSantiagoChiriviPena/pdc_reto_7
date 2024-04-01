i : int = 1 #constante denominador
if __name__ == "__main__":
    try: 
        n : int = int(input("Por favor, ingrese un numero entero entre 2 y 50: ")) #ingreso de entero n dentro del rango
        while n < 2 or n > 50:
            n = int(input("El numero ingresado no se encuentra dentro del rango establecido, por favor intentelo de nuevo: "))
        while i <= n:   #rango para la evaluacion de denominadores hasta n/n
            divisor = n/i
            if divisor % 1 == 0: #condicion para que i sea divisor de n
                print(f"{i} es divisor de {n}")
            i += 1      #escalado para el denominador
    except ValueError:
        print("El numero ingresado no se trata de un numero entero")