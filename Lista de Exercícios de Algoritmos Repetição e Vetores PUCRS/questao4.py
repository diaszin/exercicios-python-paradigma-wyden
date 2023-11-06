tamanho_chico = 1.50
tamanho_ze =  1.10
qntds_anos = 0

while True:
    tamanho_chico += 0.02
    tamanho_ze += 0.03
    qntds_anos +=1
    if tamanho_ze > tamanho_chico:
        break

print(f"É necessário {qntds_anos} anos para Zé ficar maior que Chico")