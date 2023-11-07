valor_ingresso = 5.0
ingresso_vendidos = 120
lucro_maximo = valor_ingresso*ingresso_vendidos

print("Tabela de Preço e Lucro")
while valor_ingresso >= 1.0:
    print(f"{valor_ingresso}--------{ingresso_vendidos}")
    valor_ingresso -= 0.50
    ingresso_vendidos += 26


print(f"Lucro máximo esperado: {valor_ingresso*ingresso_vendidos}\nPreço do ingresso para o lucro máximo esperado: {valor_ingresso}\nQuantidade de ingresso para o lucro máximo esperado: {ingresso_vendidos}")
