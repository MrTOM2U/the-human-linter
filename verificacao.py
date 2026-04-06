def verificar_maioridade(idade):
    # Correção: Nome da função em snake_case
    limite_idade = 18
    
    # Correção: Operador >= para incluir quem tem 18 anos
    if idade >= limite_idade:
        return "Maior de idade"
    else:
        return "Menor de idade"