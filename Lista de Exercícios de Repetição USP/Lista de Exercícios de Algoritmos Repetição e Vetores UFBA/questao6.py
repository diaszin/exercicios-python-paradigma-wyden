def cadastrar_pessoa(clientes: list):
    nome = str(input("Digite o nome completo: "))
    rg = str(input("Digite o RG: "))
    cpf = str(input("Digite o CPF: "))
    telefone = str(input("Digite o telefone: "))
    
    clientes.append({
        "nome": nome,
        "rg": rg,
        "cpf": cpf,
        "telefone": telefone
    })
    


clientes = []
while True:
    cadastrar_pessoa(clientes)
    resp = str(input("Quer continuar? [S/N]: ")).upper()
    if resp == "N":
        break


for cliente in clientes:
    print(f"{cliente['nome']} - {cliente['rg']} - {cliente['cpf']} - {cliente['telefone']}")
    