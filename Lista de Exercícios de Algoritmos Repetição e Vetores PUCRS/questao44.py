
maior_indice = -1
menor_indice = float('inf')
cidade_maior_indice = ""
cidade_menor_indice = ""


total_veiculos = 0
total_acidentes_rs = 0
num_cidades_rs = 0

for i in range(1, 201):
    print(f"Digite os dados da cidade {i}:")
    codigo = int(input("Código da cidade: "))
    estado = input("Estado (RS, SC, PR, SP, RJ, ...): ")
    num_veiculos = int(input("Número de veículos de passeio (em 1992): "))
    num_acidentes = int(input("Número de acidentes com vítimas (em 1992): "))

   
    if num_acidentes > maior_indice:
        maior_indice = num_acidentes
        cidade_maior_indice = codigo
    if num_acidentes < menor_indice:
        menor_indice = num_acidentes
        cidade_menor_indice = codigo

    total_veiculos += num_veiculos


    if estado == "RS":
        total_acidentes_rs += num_acidentes
        num_cidades_rs += 1


media_veiculos = total_veiculos / 200


media_acidentes_rs = total_acidentes_rs / num_cidades_rs


print(f"O maior índice de acidentes de trânsito é {maior_indice} na cidade {cidade_maior_indice}.")
print(f"O menor índice de acidentes de trânsito é {menor_indice} na cidade {cidade_menor_indice}.")
print(f"A média de veículos nas cidades brasileiras é {media_veiculos}.")
print(f"A média de acidentes com vítimas no estado do Rio Grande do Sul é {media_acidentes_rs}.")
