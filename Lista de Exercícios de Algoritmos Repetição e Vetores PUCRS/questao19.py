contador_media = 0
soma_pares = 0
soma_geral = 0
contador_pares = 0
contador_impares = 0



while True:
    n = int(input("Digite um nuemro qualquer positivo(ou 0 para encerrar...)  "))
    if n > 0:

        if n % 2 == 0:
            contador_pares += 1
            contador_media += 1
            soma_pares += n
            soma_geral += n
        else:
            contador_impares += 1
            contador_media += 1
            soma_geral += n
        
    else: 
        break

media_pares = soma_pares/contador_pares
media_geral = soma_geral/contador_media

print(f"Foram lidos uma quantidade de {contador_pares} numeros pares!\nForam lidos uma quantidade de {contador_impares} numeros impares!\nA media entre os numeros pares foi de {media_pares} \nA media geral foi de {media_geral} ")