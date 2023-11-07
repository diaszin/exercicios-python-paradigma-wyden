numeros_primos = [2, 3, 5]
n_atual = 5


while len(numeros_primos) < 20:
    candidato = n_atual + 2
    primo = True

    for divisor in range(2, candidato):
        if candidato % divisor == 0:
            primo = False
            break
    if primo:
        numeros_primos.append(candidato)
    n_atual = candidato
print("Os 20 primeiros números primos são:")
for numero in numeros_primos:
    print(numero)
