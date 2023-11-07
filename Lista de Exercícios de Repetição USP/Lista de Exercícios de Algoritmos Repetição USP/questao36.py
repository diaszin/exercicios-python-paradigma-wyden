def cadastrar_pessoa():
    global pessoas
    idade = int(input("Digite a idade: "))
    if idade <=0:
        return False
    else:
        altura = float(input("Digite o peso: "))
        pessoas.append({
            "idade": idade,
            "altura": altura
        })


def calcular_media_altura():
    global pessoas
    soma_altura = 0
    quantidade_pessoas_superiores_a_50 = 0
    for pessoa in pessoas:
        if pessoa.get("altura") and pessoa.get("idade") is not None and pessoa.get("idade") > 50:
            soma_altura += pessoa["altura"]
            quantidade_pessoas_superiores_a_50 += 1
    
    media = soma_altura/quantidade_pessoas_superiores_a_50
    return media  
    
pessoas = []

while True:
    if cadastrar_pessoa() == False:
        break


media = calcular_media_altura()
print(f"A média é {media}")