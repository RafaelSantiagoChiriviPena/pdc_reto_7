if __name__ == "__main__":
    try:
        n : int = int(input("Por favor, ingrese un entero: "))    #ingreso de entero n
        while n < 2:
            n = int(input("El entero ingresado debe ser mayor o igual que 2, por favor intentelo de nuevo"))
        if n%2 != 0: #de impar a par
            n -= 1
        if n%2 == 0:
            while n >= 2: # condicion del ejercicio  
                print(n)
                n -= 2 #escalado para la variable
    except ValueError:
        print("El valor ingresado no se trata de un numero entero")