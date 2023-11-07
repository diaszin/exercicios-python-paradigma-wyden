
produto = 1


for num in range(92, 1479):
    if num < 2:
        continue  
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        produto *= num


print("O produto dos números primos entre 92 e 1478 é:", produto)
