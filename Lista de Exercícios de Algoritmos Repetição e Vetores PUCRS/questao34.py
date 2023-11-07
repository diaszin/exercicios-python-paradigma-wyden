maior_altura = -1
menor_altura = 999
cod_maior_aluno = 0
cod_menor_aluno = 0

for i in range (5):
    num_aluno = int(input("\nDigite o numero do aluno ->  "))
    altura = int(input("\nDigite a altura do aluno sem centimetros ->  "))
    if altura > maior_altura:
        maior_altura = altura
        cod_maior_aluno = num_aluno
    if altura < menor_altura:
        menor_altura = altura
        cod_menor_aluno = num_aluno

print(f"O aluno {cod_maior_aluno} com a altura de {maior_altura} foi eleito o maior aluno.\nO aluno {cod_menor_aluno} com a altura de {menor_altura} foi eleito o menor aluno.")

