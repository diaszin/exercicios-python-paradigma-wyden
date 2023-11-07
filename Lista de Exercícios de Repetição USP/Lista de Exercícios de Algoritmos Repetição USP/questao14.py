quantidae_pessoas = 20
quantidade_pessoas_com_mais_50_anos_e_menor_que_60_quilos = 0
soma_das_idades_pessoas_menores_que_1_50 = 0
quantidade_pessoas_menores_que_1_50 = 0
quantidae_pessoas_olhos_azuis = 0
quantidade_pessoas_que_sao_ruivas_e_nao_tem_olhos_azuis = 0


for pessoa in range(quantidae_pessoas):
    idade = int(input("Digite a idade da pessoa: "))
    peso = float(input("Digite o peso da pessoa: "))
    altura = float(input("Digite o altura da pessoa"))
    cor_dos_olhos =  str(input("Digite a cor do olhos da pessoa\nA-azul\nC-Castanho\nP-Preto\nV-Verde\n -> "))
    cor_cabelo =  str(input("Digite a cor do cabelo da pessoa\nR-Ruivo\nC-Castanho\nP-Preto\nL-Louro\n -> "))
    
    if idade >= 50 and peso <= 60:
        quantidade_pessoas_com_mais_50_anos_e_menor_que_60_quilos +=1
    if altura <= 1.50:
        soma_das_idades_pessoas_menores_que_1_50 +=idade
        quantidade_pessoas_menores_que_1_50 += altura
        
    if cor_cabelo == "R" and cor_dos_olhos != ["A"]:
        quantidade_pessoas_que_sao_ruivas_e_nao_tem_olhos_azuis += 1
    if cor_dos_olhos == ["A"]:
        quantidae_pessoas_olhos_azuis +=1


print(f"Existe {quantidade_pessoas_com_mais_50_anos_e_menor_que_60_quilos} pessoas que tem uma idade maior que 50 anos e pesa menos que 60 quilos")
print(f"A média da idade das pessoas que possuem a altura menor que 1,50 é de {(soma_das_idades_pessoas_menores_que_1_50/quantidade_pessoas_menores_que_1_50)}")
print(f"As pessoas com olhos azuis ocupam {format((quantidae_pessoas_olhos_azuis/quantidae_pessoas)*100, '.1f')}%")
print(f"A quantidade de pessoas que tem cabelo ruivo e não tem olhos azuis é de {quantidade_pessoas_que_sao_ruivas_e_nao_tem_olhos_azuis}")
