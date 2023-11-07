from datetime import datetime


def diferenca_entre_datas(data1, data2):
    data1 = datetime.strptime(data1, "%d-%m-%Y")
    data2 = datetime.strptime(data2, "%d-%m-%Y")
    diferenca = data2 - data1
    return diferenca.days


data1 = input("Digite a primeira data (DD-MM-AAAA): ")
data2 = input("Digite a segunda data (DD-MM-AAAA): ")


dias_de_diferenca = diferenca_entre_datas(data1, data2)


print(f"A diferença entre as datas é de {dias_de_diferenca} dias.")
