numero_pessoas = 7
quantidade_pessoa_feminino = 0
quantidade_pessoa_masculino = 0
soma_idades_masculino = 0
soma_idades_feminino = 0


for num in range(numero_pessoas):
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo: "))[0].upper()
    
    if sexo == "M":
        quantidade_pessoa_masculino +=1
        soma_idades_masculino += idade
    if sexo == "F":
        quantidade_pessoa_feminino +=1
        soma_idades_feminino += idade

soma_idade = soma_idades_feminino+soma_idades_masculino
print(f"Idade média do grupo: {soma_idade/numero_pessoas}")
print(f"Idade média masculino: {soma_idades_masculino/quantidade_pessoa_masculino}")
print(f"Idade média feminino: {soma_idades_feminino/quantidade_pessoa_feminino}")