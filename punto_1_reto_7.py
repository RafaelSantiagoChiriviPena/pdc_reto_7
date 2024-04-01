i : int = 1     # se indica una constante i a la cual anclar el while
if __name__ == "__main__":
    while i <= 100:     # condicion del ejercicio 
        i_cuadrado = i ** 2     # operacion de cuadrado para i
        print(f"EL cuadrado de {i} es {i_cuadrado}")
        i += 1      # escalado para la constante