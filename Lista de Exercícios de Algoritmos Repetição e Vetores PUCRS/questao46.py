
maior_idade = 0
contagem_feminino_18_35_verdes_louros = 0


for i in range(1, 501):
    sexo = input("Digite o sexo (M - masculino, F - feminino): ")
    cor_olhos = input("Digite a cor dos olhos (A - azuis, V - verdes, C - castanhos): ")
    cor_cabelos = input("Digite a cor dos cabelos (L - louros, C - castanhos, P - pretos): ")
    idade = int(input("Digite a idade: "))


    if idade > maior_idade:
        maior_idade = idade

   
    if sexo == "F" and idade >= 18 and idade <= 35 and cor_olhos == "V" and cor_cabelos == "L":
        contagem_feminino_18_35_verdes_louros += 1

print(f"Maior idade do grupo: {maior_idade} anos")
print(f"Quantidade de indivíduos do sexo feminino, entre 18 e 35 anos, com olhos verdes e cabelos louros: {contagem_feminino_18_35_verdes_louros}")
