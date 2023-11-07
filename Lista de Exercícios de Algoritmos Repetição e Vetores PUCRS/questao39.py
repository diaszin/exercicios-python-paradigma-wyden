num_perfeitos = []  
num = 2  

while len(num_perfeitos) < 5:
    soma_divisores = 1  

  
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            
            soma_divisores += divisor
            outro_divisor = num // divisor
            if outro_divisor != divisor:
                soma_divisores += outro_divisor

  
    if soma_divisores == num:
        num_perfeitos.append(num)

    num += 1


print("Os 5 primeiros números perfeitos são:")
for numero_perfeito in num_perfeitos:
    print(numero_perfeito)