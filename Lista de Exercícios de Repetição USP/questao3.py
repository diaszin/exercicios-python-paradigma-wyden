print("--Tabuada--")
for numero in range(11):
    print("Tabuada do número:", numero)
    for numero_a_ser_multiplicado in range(11):
        resultado = numero * numero_a_ser_multiplicado
        print(numero, "x", numero_a_ser_multiplicado, "=", resultado)
