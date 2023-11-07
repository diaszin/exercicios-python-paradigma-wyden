def cadastrar_pessoa(pessoas: list):
    valor_base_indenizacao = float(
        input("Digite o valor base da indenização: "))
    idade_paciente = int(input("Digite a idade do paciente: "))
    nome_completo = str(input("Digite o nome completo do paciente: "))

    if idade_paciente > 0:
        aumento_porcentagem = 0
        if idade_paciente <= 12:
            aumento_porcentagem = 30/100
        elif idade_paciente >= 13 and idade_paciente <= 49:
            aumento_porcentagem = 10/100
        elif idade_paciente >= 50 and idade_paciente <= 65:
            aumento_porcentagem = 15/100
        else:
            aumento_porcentagem = 35/100

        reajuste = valor_base_indenizacao + \
            (valor_base_indenizacao*aumento_porcentagem)
        pessoas.append({
            "nome": nome_completo,
            "idade": idade_paciente,
            "valor_base": valor_base_indenizacao,
            "reajuste": reajuste
        })
    else:
        print("Idade inválida, pessoa não será cadastrada  !")

pessoas = []
qntd_vezes = int(input("Digite quantas pessoas deseja cadastrar: "))
if qntd_vezes > 0:
    for i in range(qntd_vezes):
        cadastrar_pessoa(pessoas)
    print("nome - idade - reajuste".upper())
    for pessoa in pessoas:
        linha_pessoa = f"{pessoa['nome']} - {pessoa['idade']} - R${format(pessoa['reajuste'], '.2f')}"
        sep = "="*len(linha_pessoa)
        print(sep)
        print(linha_pessoa)
        print(sep)
        
else:
    print("Quantidade de vezes inválida, tente novamente")