import random

soma_idades = 0
quantidade_pessoas = 7
quantidade_pessoas_com_mais_de_90_quilos = 0

for pessoa in range(quantidade_pessoas):
    #idade = int(input("Digite a idade da pessoa: "))
    #peso = float(input("Digite o peso da pessoa: "))
    idade = random.randint(0, 100)
    peso = random.uniform(20, 120)
    
    if peso >=90:
        quantidade_pessoas_com_mais_de_90_quilos +=1
    soma_idades += idade


print(f"A média das idades das pessoas é: {round(soma_idades/quantidade_pessoas)}")
print(f"Existem {quantidade_pessoas_com_mais_de_90_quilos} de pessoas com mais de 90 quilos")