index = 10
somas_das_idades = 0
quantidade_de_pessoas_com_peso_de_90_e_altura_menor_que_1_50 = 0
quantidade_pessoas_que_tem_entre_10_e_30_anos_e_mede_mais_que_1_90 = 0


for num in range(index):
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    
    if peso >=90 and altura < 1.50:
        quantidade_de_pessoas_com_peso_de_90_e_altura_menor_que_1_50 +=1
    if (idade >= 10 and idade <=30) and altura >= 1.90:
        quantidade_pessoas_que_tem_entre_10_e_30_anos_e_mede_mais_que_1_90 +=1


print(f"A média das pessoas é {somas_das_idades/index}")
print(f"Existe {quantidade_de_pessoas_com_peso_de_90_e_altura_menor_que_1_50} pessoas que tem um peso maior que 90 kilos e menor que 1,50 ")
print(f"A porcentagem de pessoas que tem idade entre 10 e 30 e são maiores que 1,90 é {quantidade_pessoas_que_tem_entre_10_e_30_anos_e_mede_mais_que_1_90*index/100}")