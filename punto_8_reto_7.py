def primo (n : int = 1, i : int = 1,) -> str:
    while n <= 100:     #delimitacion del rango 1 a 100
        i = 1
        while i <= n - 1: #rango para la evaluacion de denominadores hasta n/n
            divisor = n / i
            if divisor % 1 == 0 and n == 2:     #caso especial n = 2 siendo primo
                print(f"{n} es un numero primo \n")
            if divisor % 1 == 0 and i != 1:     #condicion para no primos, excluyendo a n/1
                print(f"{n} no es un numero primo \n")
                break
            if divisor % 1 != 0 and i == n - 1: #condicion para primos
                print(f"{n} es un numero primo \n")
            i += 1  #escalado para el denominador
        n = n + 1   #escalado de 1 a 100
if __name__ == "__main__":
    primo()