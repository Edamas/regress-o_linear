# regressao_linear

Método dos mínimos quadrados (MMQ)
----------------------------------
Fórmula da Regressão linear
(é a ``fórmula da reta``:)

``y = A + Bx``

``A``: Intercepto

``B``: Coeficiente Angular



## Exemplo de uso:
````
x = [1, 2, 0]
y = [4, 7, 3]
a, b = regressao_linear(
    serie_x=x, 
    serie_y=y
    )
print('Intecepto:          ', a)
print('Coeficiente angular:', b)
print(f'Fórmula da reta (y = A + B * x):')
print(f'                 y = {a} + {b} * x')
````

## Resultado:

``Intecepto:           2.6666666666666665``

``Coeficiente angular: 2.0``

``Fórmula da reta (y = A + B * x):``

``                 y = 2.6666666666666665 + 2.0 * x``
                 
