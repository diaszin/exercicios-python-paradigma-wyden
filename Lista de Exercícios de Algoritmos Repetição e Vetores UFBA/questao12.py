def calcular_quantidade_elementos_em_um_intervalo(vetor: list,a:  int, b:int):
    quantidade = 0
    for num in vetor:
        if num >=a and num <=b:
            quantidade +=1
    
    return quantidade

vetor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


a = int(input("Digite o número que quer começar: "))
b = int(input("Digite o número que quer terminar: "))

quantidade = calcular_quantidade_elementos_em_um_intervalo(vetor, a, b)
print(f"Existe {quantidade} números no vetor entre {a} e {b}")