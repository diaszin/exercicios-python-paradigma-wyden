m = 0
somatorio_negativos = 0

while True:
    m = int(input("insira um numero inteiro (ou Digite 0 para encerrar!) "))

    if m == 0:
        break
    if m < 0:
        somatorio_negativos += m

print(f"A soma dos numeros negativos foi de {somatorio_negativos}")