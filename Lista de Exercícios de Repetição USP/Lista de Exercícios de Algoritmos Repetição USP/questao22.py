quantidade_pessoas = 15

faixa_etaria_1 = 0  # Faixa etaria entre 1 e 10
faixa_etaria_2 = 0  # Faixa etaria entre 11 e 20
faixa_etaria_3 = 0  # Faixa etaria entre 21 e 30
faixa_etaria_4 = 0 # Faixa etaria maior que 31

soma_peso_faixa_etaria_1 = 0 
soma_peso_faixa_etaria_2 = 0 
soma_peso_faixa_etaria_3 = 0 
soma_peso_faixa_etaria_4 = 0

for pessoa in range(quantidade_pessoas):
    idade = int(input("Digite a idade da pessoa: "))
    peso = int(input("Digite o peso da pessoa: "))
    
    if(idade >= 1 and idade <=10):
        soma_peso_faixa_etaria_1 += peso
        faixa_etaria_1 +=1
    elif(idade >= 11 and idade <= 20):
        soma_peso_faixa_etaria_2 += peso
        faixa_etaria_2 +=1
    elif(idade >= 21 and idade <= 30):
        soma_peso_faixa_etaria_3 += peso
        faixa_etaria_3 +=1
    elif(idade >= 31):
        soma_peso_faixa_etaria_4 += peso
        faixa_etaria_4 +=1
        
media_faixa_etaria_1 = soma_peso_faixa_etaria_1/faixa_etaria_1
media_faixa_etaria_2 = soma_peso_faixa_etaria_2/faixa_etaria_2
media_faixa_etaria_3 = soma_peso_faixa_etaria_3/faixa_etaria_3
media_faixa_etaria_4 = soma_peso_faixa_etaria_4/faixa_etaria_4

print(f"""
A média dos pesos das pessoas entre 1 e 10: {media_faixa_etaria_1}      
A média dos pesos das pessoas entre 11 e 20: {media_faixa_etaria_2}      
A média dos pesos das pessoas entre 21 e 30: {media_faixa_etaria_3}      
A média dos pesos das pessoas maior que 31: {media_faixa_etaria_4}      
""")