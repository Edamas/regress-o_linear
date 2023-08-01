def regressao_linear(serie_x, serie_y):
    '''
    Fórmula da Regressão linear 
    Método dos mínimos quadrados (MMQ):
    
    y = A + Bx
    
    A: Intercepto
    B: Coeficiente Angular
    (é a fórmula da reta)
    '''
    
    # ambas as séries devem possuir o mesmo número de elementos
    assert len(serie_x) == len(serie_y)  
    
    # Cálculos comuns:
    n = len(serie_x)
    soma_x = sum(x)
    soma_y = sum(y)
    soma_xx = sum([i ** 2 for i in x])
    soma_yy = sum([i ** 2 for i in y])
    soma_xy = sum([i * j for i, j in zip(x, y)])
    
    
    # Calculando o coeficiente angular (B)
    assert 0 != n * soma_xx - soma_x ** 2
    B = (n * soma_xy - soma_x * soma_y) / (n * soma_xx - soma_x ** 2)
    
    # Calculando o intercepto (A)
    A = (soma_y - B * soma_x) / n
    
    return A, B

def main():
  # Exemplo:
  
  # 2 Séries:
  x = [1, 2, 0]
  y = [4, 7, 3]
  
  # Cálculo da Função Linear
  a, b = regressao_linear(
      serie_x=x, 
      serie_y=y
      )
  
  print('Intecepto:          ', a)
  print('Coeficiente angular:', b)
  print(f'Fórmula da reta (y = A + B * x):')
  print(f'                 y = {a} + {b} * x') 

if __name__ == '__main__':
  main()
