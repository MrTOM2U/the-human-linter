def calcular_total(preco, taxa):
    # Correção: snake_case e espaços adequados
    imposto = preco * taxa
    
    # Correção: Lógica de soma do imposto ao preço
    resultado = preco + imposto
    
    return resultado