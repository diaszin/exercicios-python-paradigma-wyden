qntd_espectador = 15
qntd_respostas_otimas = 0
soma_idade_que_responderam_otimo = 0
qntd_pessoas_que_responderam_regular = 0
qntd_pessoas_que_responderam_bom = 0


for espectador in range(qntd_espectador):
    idade = int(input("Digite a idade do espectador"))
    escolha_opniao = int(input("Digite a sua opnião\n1-Regular\2-Bom\n30-Ótimo\n:"))
    if(escolha_opniao ==1):
        qntd_pessoas_que_responderam_regular +=1
    elif(escolha_opniao ==2):
        qntd_pessoas_que_responderam_bom +=1
    elif(escolha_opniao ==3):
        soma_idade_que_responderam_otimo +=idade
        qntd_respostas_otimas +=1
    else:
        continue
    


print(f"""
media das idades das pessoas que responderam ótimo: {soma_idade_que_responderam_otimo/qntd_respostas_otimas}
porcentagem de pessoas que responderam bom: {qntd_pessoas_que_responderam_bom/qntd_espectador*100} 
quantidade de pessoas que responderam regular: {qntd_pessoas_que_responderam_regular}
""")