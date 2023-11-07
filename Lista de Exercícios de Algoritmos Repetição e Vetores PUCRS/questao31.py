valor = 0
contador_intervalo = 0
contador_fora_intervalo = 0

for i in range (10):
    valor = int(input("Digite um numero qualquer ->  "))
    if valor >= 10 and valor >= 20:
        contador_intervalo += 1
    else:
        contador_fora_intervalo += 1

print(f"Existiram {contador_intervalo} numeros no intervalo de 10 ate 20\nExistiram {contador_fora_intervalo} numeros fora do intervalo.")