def cadastrar_pessoas():
    global dados

    salario = float(input("Digite o salário: "))
    if salario < 0:
        return False
    else:
        idade = int(input("Digite a idade: "))
        sexo = cadastrar_sexo()

        dados.append({
            "idade": idade,
            "sexo": sexo,
            "salario": salario,
        })
        return True


def cadastrar_sexo():
    while True:
        sexo = str(input("Digite o sexo [M/F]: ")).upper()[0]
        if sexo in ["M", "F"]:
            return sexo
        else:
            print("Insira um gênero correto !")


def media_salario_geral():
    global dados
    soma_salario = 0
    for pessoa in dados:
        soma_salario += pessoa["salario"]

    media = soma_salario/len(dados)
    return media


def maior_e_menor_idade_do_grupo():
    global dados
    maior_idade = None
    menor_idade = None

    for pessoa in dados:
        idade = pessoa["idade"]
        if maior_idade == None or maior_idade < idade:
            maior_idade = idade
        if menor_idade == None or menor_idade > idade:
            menor_idade = idade

    return (maior_idade, menor_idade,)


def mulheres_com_salario_ate_200():
    global dados
    quantidade_mulheres = 0
    for pessoa in dados:
        if pessoa["sexo"] == "F" and pessoa["salario"] <= 200:
            quantidade_mulheres += 1

    return quantidade_mulheres


def pessoa_com_menor_salario():
    global dados
    menor_salario = None
    pessoa_menor_salario = None
    for pessoa in dados:
        if menor_salario == None or pessoa["salario"] < menor_salario:
            pessoa_menor_salario = {
                "idade": pessoa["idade"],
                "sexo": pessoa["sexo"]
            }

    return pessoa_menor_salario


dados = []

while True:
    if cadastrar_pessoas() == False:
        break

media_salario = media_salario_geral()
maior_idade, menor_idade = maior_e_menor_idade_do_grupo()
quantidade_mulheres = mulheres_com_salario_ate_200()
pessoa_menor_salario = pessoa_com_menor_salario()
print(f"""
A media do salario do grupo: {media_salario}
A maior idade do grupo: {maior_idade}
A menor idade do grupo: {menor_idade}
Quantidade de mulheres que tem um salário de até 200 reais: {quantidade_mulheres}
A idade e o sexo do menor salário do grupo:
  - Sexo: {pessoa_menor_salario["sexo"]}
  - Idade: {pessoa_menor_salario["idade"]}
""")