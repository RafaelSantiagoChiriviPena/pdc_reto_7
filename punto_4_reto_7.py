A : float = 25000000    #constante de poblacion A
B : float = 18900000    #constante de poblacion B
anio = 2022
if __name__ == "__main__":
    print(f"para el año {anio} el pais A tiene una poblacion de {A} habitantes, mientras que el pais B cuenta con {B} habitantes \n habiendo una diferencia de {A - B} habitantes")
    while B < A:    # condicion del ejercicio 
        A += (A * 2) / 100      # crecimiento poblacional A
        B += (B * 3) / 100      # crecimiento poblacional B
        anio += 1   # escalado para la constante año
    print(f"para el año {anio} el pais A tiene una poblacion de {A} habitantes, mientras que el pais B cuenta con {B} habitantes \n habiendo una diferencia de {B - A}")