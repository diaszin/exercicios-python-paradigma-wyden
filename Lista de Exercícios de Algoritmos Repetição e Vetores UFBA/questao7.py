def contagem_numeros_pares(vetor: list):
    contagem_numero_par = 0
    for numero in vetor:
        if numero % 2 == 0:
            contagem_numero_par +=1
    
    return contagem_numero_par

vetor = []
qntd_vezes = 10
for i in range(qntd_vezes):
    num = int(input("Digite o número: "))
    vetor.append(num)
    

quantidade_numero_par = contagem_numeros_pares(vetor)

print(f"Existe {quantidade_numero_par} números pares na lista")    