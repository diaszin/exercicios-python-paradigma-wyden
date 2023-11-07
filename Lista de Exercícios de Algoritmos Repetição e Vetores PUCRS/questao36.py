n = 0
fatorial = 0

n = int(input("Digite quantos numeros serao calculados ->  "))
for i in range(n):
    numero = int(input("Digite o numero no qual sera calculado o fatorial ->  "))
    contador = numero - 1
    fatorial = numero
    for x in range(1, numero):
        print(f"{fatorial} x {contador} ")
        fatorial *= contador
        contador -= 1
        
        

    print(f"O valor lido foi {numero} e o seu fatorial é {fatorial}")
    
    
