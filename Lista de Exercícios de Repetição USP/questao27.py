def percentagem_pessoas(canais: dict, quantidade_pessoas: int):
    for canal, quantidade in canais.items():
        porcentagem = (quantidade / quantidade_pessoas) * 100
        print("-"*100)
        print(f"O Canal {canal} tem {format(porcentagem, '.2f')}%")
        print("-"*100)


canais = {}
quantidade_pessoas = 0

while True:
    numero_canal = int(input("Digite o número do canal: "))
    if numero_canal == 0:
        break
    
    else:
        numero_pessoas = int(input("Digite o número de pessoas: "))
        if numero_canal in [4, 5, 7, 12]:
            canais[numero_canal] = numero_pessoas
        
        quantidade_pessoas += numero_pessoas


percentagem_pessoas(canais, quantidade_pessoas)
