def calcular_media_idade(idades: list) -> int:
    soma_idades = 0
    for idade in idades:
        soma_idades += idade
    
    media = soma_idades/len(idades)
    return round(media)



idades = []

while True:
    idade = int(input("Digite sua idade: "))
    if idade > 0:
        idades.append(idade)
    else:
        break

media = calcular_media_idade(idades)
print(media)