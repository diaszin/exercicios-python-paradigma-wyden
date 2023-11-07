quantidade_de_primeira_faixa_etaria = 0
quantidade_de_segunda_faixa_etaria = 0
quantidade_de_terceira_faixa_etaria = 0
quantidade_de_quarta_faixa_etaria = 0
quantidade_de_quinta_faixa_etaria = 0

quantidade_pessoas = 15

for num in range(quantidade_pessoas):
    idade_pessoa = int(input("Digite a idade da pessoa: "))
    if idade_pessoa <= 15:
        quantidade_de_primeira_faixa_etaria += 1
    elif idade_pessoa >= 16 and idade_pessoa <= 30:
        quantidade_de_segunda_faixa_etaria += 1
    elif idade_pessoa >= 31 and idade_pessoa <= 45:
        quantidade_de_terceira_faixa_etaria += 1
    elif idade_pessoa >= 46 and idade_pessoa <= 60:
        quantidade_de_quarta_faixa_etaria += 1
    else:
        quantidade_de_quinta_faixa_etaria += 1


print(f"Existem {quantidade_de_primeira_faixa_etaria} pessoas na 1º Faixa Etária - Representando {format((quantidade_de_primeira_faixa_etaria/quantidade_pessoas)*100, '.2f')}% da quantidade de pessoas")
print(f"Existem {quantidade_de_segunda_faixa_etaria} pessoas na 2º Faixa Etária - Representando {format((quantidade_de_segunda_faixa_etaria/quantidade_pessoas)*100, '.2f')}% da quantidade de pessoas")
print(f"Existem {quantidade_de_terceira_faixa_etaria} pessoas na 3º Faixa Etária - Representando {format((quantidade_de_terceira_faixa_etaria/quantidade_pessoas)*100, '.2f')}% da quantidade de pessoas")
print(f"Existem {quantidade_de_quarta_faixa_etaria} pessoas na 4º Faixa Etária - Representando {format((quantidade_de_quarta_faixa_etaria/quantidade_pessoas)*100, '.2f')}% da quantidade de pessoas")
print(f"Existem {quantidade_de_quinta_faixa_etaria} pessoas na 5º Faixa Etária - Representando {format((quantidade_de_quinta_faixa_etaria/quantidade_pessoas)*100, '.2f')}% da quantidade de pessoas")

