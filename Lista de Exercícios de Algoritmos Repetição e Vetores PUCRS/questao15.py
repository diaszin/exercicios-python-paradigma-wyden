qntd_numeros_entre_0_e_25 = 0
qntd_numeros_entre_26_e_50 = 0
qntd_numeros_entre_51_e_75 = 0
qntd_numeros_entre_76_e_100 = 0

while True:
    num = int(input("Digite o número: "))
    if num < 0:
        break
    else:
        if num >= 0 and num <= 25:
            qntd_numeros_entre_0_e_25 += 1
        elif num >= 26 and num <=50:
            qntd_numeros_entre_26_e_50 +=1
        elif num >= 51 and num <=75:
            qntd_numeros_entre_51_e_75 +=1
        elif num >= 76 and num <= 100:
            qntd_numeros_entre_76_e_100 +=1

print(f"""
Existem {qntd_numeros_entre_0_e_25} números no intervalo de 0 e 25
Existem {qntd_numeros_entre_26_e_50} números no intervalo de 26 e 50
Existem {qntd_numeros_entre_51_e_75} números no intervalo de 51 e 75
Existem {qntd_numeros_entre_76_e_100} números no intervalo de 76 e 100
""")