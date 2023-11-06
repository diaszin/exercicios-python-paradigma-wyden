qntd_vezes = 50
maior_numero = None
menor_numero = None

for vez in range(qntd_vezes):
    numero = int(input("Digite o número: "))
    if maior_numero is None or maior_numero < numero:
        maior_numero = numero
    if menor_numero is None or menor_numero > numero:
        menor_numero = numero



print(f"O Maior Número é: {maior_numero} - O Menor Número é: {menor_numero}")
