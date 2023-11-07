
soma_idade = 0
soma_altura_mulheres = 0
soma_idade_homens = 0
contagem_total = 0
contagem_mulheres = 0
contagem_homens = 0
contagem_idade_entre_18_e_35 = 0


for i in range(1, 1001):
    sexo = int(input("Digite o sexo (0 - feminino, 1 - masculino): "))
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura (em metros): "))

  
    soma_idade += idade

  
    if sexo == 0:
        soma_altura_mulheres += altura
        contagem_mulheres += 1

 
    if sexo == 1:
        soma_idade_homens += idade
        contagem_homens += 1

  
    if idade >= 18 and idade <= 35:
        contagem_idade_entre_18_e_35 += 1

    contagem_total += 1


media_idade = soma_idade / contagem_total
media_altura_mulheres = soma_altura_mulheres / contagem_mulheres if contagem_mulheres > 0 else 0
media_idade_homens = soma_idade_homens / contagem_homens if contagem_homens > 0 else 0
percentual_idade_entre_18_e_35 = (contagem_idade_entre_18_e_35 / contagem_total) * 100


print(f"Média da idade do grupo: {media_idade:.2f} anos")
print(f"Média da altura das mulheres: {media_altura_mulheres:.2f} metros")
print(f"Média da idade dos homens: {media_idade_homens:.2f} anos")
print(f"Percentual de pessoas com idade entre 18 e 35 anos: {percentual_idade_entre_18_e_35:.2f}%")
