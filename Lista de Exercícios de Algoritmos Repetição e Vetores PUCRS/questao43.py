
def calcular_total(grupo):
    return grupo[0] + grupo[1] + grupo[2] + grupo[3]


grupos = []


for i in range(5):
    grupo = []
    print(f"Digite os valores para o Grupo {i + 1}:")
    for j in range(4):
        valor = float(input(f"Digite o valor {j + 1}: "))
        grupo.append(valor)
    grupos.append(grupo)


print("\nGrupos na Ordem Lida:")
for i, grupo in enumerate(grupos):
    print(f"Grupo {i + 1}: {grupo}")


grupos.sort(key=calcular_total, reverse=True)


print("\nGrupos Ordenados em Ordem Decrescente:")
for i, grupo in enumerate(grupos):
    print(f"Grupo {i + 1}: {grupo}")

