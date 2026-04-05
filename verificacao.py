def Verificar_Maioridade(idade):
    limite_idade=18
  
    if idade > limite_idade:
        return "Maior de idade"
    else:
        return "Menor de idade"

print(Verificar_Maioridade(18))