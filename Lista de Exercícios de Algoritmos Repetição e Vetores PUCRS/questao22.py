contador = 0
salario_baixo_mulheres = 0
m_salario_geral = 0
idade_maior = -1
idade_menor = 99999


while True:
    idade = int(input("Insira a idade do individuo do grupo (ou uma idade negativa qualquer para encerrar...): "))
    if idade < 0:
        break
        
    if idade > idade_maior:
        idade_maior = idade
    if idade < idade_menor:
        idade_menor = idade

    sexo = input("Sexo M/F").upper()

    salario = float(input("Digite o salario em R$: "))
    m_salario_geral += salario
    contador += 1
    if sexo == "F" and salario <= 100:
        salario_baixo_mulheres += 1

m_salario_geral = m_salario_geral/contador
print(f"A Media salarial do grupo foi de R${m_salario_geral:.2f}\nA maior idade foi de {idade_maior} anos\nA menor idade foi de {idade_menor} anos\nNo grupo existem {salario_baixo_mulheres} mulheres com o salario menor de R$ 100,00 ")
                

