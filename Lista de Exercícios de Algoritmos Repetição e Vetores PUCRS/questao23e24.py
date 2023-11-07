maior_idade = -1
contador_jovens_mulheres = 0

while True:
    sexo = input("Escreva o sexo do individuo: M/F (Ou digite -1 para encerrar!)  ").upper()
    if sexo == '-1':
        break

    cor_olhos = input("Digite a cor dos olhos:  'Azuis' , 'Verdes' ou 'Castanhos' ->  ").upper()

    cor_cabelos = input("Digite a cor dos cabelos: 'Louros' , 'Castanhos' ou 'Pretos' ->  ").upper()

    idade = int(input("Digite a idade: "))

    if idade > maior_idade:
        maior_idade = idade
    if sexo == "F" and idade >= 18 and idade <=35 and cor_olhos == "VERDES" and cor_cabelos == "LOUROS":
        contador_jovens_mulheres += 1

print(f"A maior idade foi de {maior_idade}\nExistem {contador_jovens_mulheres} individuos do sexo feminino cuja idade está entre 18 e 35 anos e que tambem tem olhos verdes e cabelos louros")

    