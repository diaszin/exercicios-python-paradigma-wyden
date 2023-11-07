resultado_n_fatorial = None
num = int(input("Digite o número fatorial a ser calculado: "))

for i in range(num+1):
    if(num == 0):
        resultado_n_fatorial = 1
    else:
        if(resultado_n_fatorial == None and i !=0):
            resultado_n_fatorial = i
        elif(i > 0):
            resultado_n_fatorial *= i
        
print(f"O resultado de fatorial é {resultado_n_fatorial}")