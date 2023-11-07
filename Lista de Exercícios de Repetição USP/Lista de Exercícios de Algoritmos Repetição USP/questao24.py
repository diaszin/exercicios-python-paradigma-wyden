qntd_pessoas = 10
qntd_pessoas_que_respondeu_sim = 0
qntd_pessoas_que_respondeu_nao = 0
qntd_mulheres_respondeu_sim = 0
qntd_homens = 0
qntd_homes_respondeu_nao = 0

for pessoa in range(qntd_pessoas):
    sexo = str(input("Digite o sexo da pessoas [M/F]: ")).upper()
    resp = str(input("Gostou do produto [S/N]: ")).upper()
    
    if(resp == "S"):
        qntd_mulheres_respondeu_sim +=1
    elif(resp == "N"):
        qntd_pessoas_que_respondeu_nao +=1
    elif(sexo == "F" and resp == "S"):
        qntd_mulheres_respondeu_sim +=1
    elif(sexo == "M"):
        if(resp == "N"):
            qntd_homes_respondeu_nao +=1
        qntd_homens +=1



print(f"""
Quantidade de pessoas que responderam sim: {qntd_pessoas_que_respondeu_sim}
Quantidade de pessoas que responderam não: {qntd_pessoas_que_respondeu_nao}
Número de mulheres que responderam sim: {qntd_mulheres_respondeu_sim}
Percentagem de homens que respnderam não: {qntd_homes_respondeu_nao/qntd_homens*100}
""")