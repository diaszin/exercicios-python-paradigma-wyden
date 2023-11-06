media_salario_populacao = 0
# Valores essenciais para o calculo da média
qntd_pessoas = 0
soma_salario = 0
soma_filhos = 0

qntd_pessoas_salario_ate_100 = 0
maior_salario = None

while True:
    salario = float(input("Digite o salário do usuário: "))
    if salario < 0:
        break
    else:
        numero_filhos = int(input("Quantos filhos possui: "))
        if maior_salario is None or salario > maior_salario:
            maior_salario = salario
        if salario <=100:
            qntd_pessoas_salario_ate_100 +=1
        soma_salario += salario
        soma_filhos += numero_filhos
        qntd_pessoas +=1
        

media_salario_populacao = soma_salario/qntd_pessoas
media_filhos_populacao = round(soma_filhos/qntd_pessoas)
percentual_pessoas_com_salario_ate_100 = qntd_pessoas_salario_ate_100/qntd_pessoas*100

print(f"""
Média de salário da população: {format(media_salario_populacao, '.2f')}
Média filhos da população: {media_filhos_populacao}
Maior Salário: {format(maior_salario, '.2f')}
Percentual de pessoas com salario de até 100 reais: {format(percentual_pessoas_com_salario_ate_100, '.2f')}%
""")