```mermaid
flowchart TD
A(inicio)
B[Leer n]
C{¿n < 2?}
D{¿n % 1 != 0?}
E[n = n - 1]
F{¿n % 1 == 0?}
J{¿n >= 2?}
G[escribir n]
H[n = n - 2]
I(fin)

A --> B
B --> C 
C -- si --> B
C -- no --> D
D -- si --> E
E --> D
D -- no --> F
F -- si --> J
J -- si --> G
G --> H
H --> J
J -- no --> I
```
