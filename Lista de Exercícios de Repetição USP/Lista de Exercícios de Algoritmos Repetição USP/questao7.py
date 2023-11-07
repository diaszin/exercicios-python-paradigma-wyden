quantidade_de_pessoas_maior_de_idade = 0

for ind in range(10):
    idade_da_pessoa = int(input("Digite a idade da pessoa: "))
    if idade_da_pessoa >= 18:
        quantidade_de_pessoas_maior_de_idade +=1


print(f"Existem {quantidade_de_pessoas_maior_de_idade} pessoas nessa lista maior que 18 anos")
