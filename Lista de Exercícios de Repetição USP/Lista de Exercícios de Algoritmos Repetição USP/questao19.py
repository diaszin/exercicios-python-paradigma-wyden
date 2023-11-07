soma_idade = 0
quantidade_de_idades = 0
idade_pessoa = None

while idade_pessoa == None or idade_pessoa != 0:
    idade_pessoa = int(input("Digite a idade da pessoa: "))
    soma_idade += idade_pessoa
    quantidade_de_idades +=1
    
media_idade = soma_idade/quantidade_de_idades

print(f"A média da idade é de {round(media_idade)}")
