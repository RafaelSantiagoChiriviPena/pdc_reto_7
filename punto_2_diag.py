```mermaid
flowchart TD
A(inicio)
B[par = 2]
C[impar = 1]
D[escribir 'numeros impares']
E{¿impar > 999?}
F[escribir impar]
G[impar = impar + 2]
L[escribir 'numeros pares']
H{¿par > 1000?}
I[escribir par]
J[par = par + 2]
K(Fin)


A --> B
B --> C
C --> D
D --> E
E -- no --> F
F --> G
G --> E
E -- si --> L
L --> H 
H -- no --> I
I --> J
J --> H
H -- si --> K
```
