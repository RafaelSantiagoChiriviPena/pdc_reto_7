```mermaid
flowchart TD
A(inicio)
B[i = 1]
C{¿i > 100?}
D[i_cuadrado=i**2]
E[escribir el cuadrado ´i´ es ´i_cuadrado´]
F[i += 1]
G(fin)


A --> B 
B --> C
C --no--> D
C --si--> G
D --> E
E --> F
F --> C
```
