
x = int(input("Digite o valor de X (inteiro positivo): "))
y = int(input("Digite o valor de Y (inteiro positivo): "))

if x < 0 or y < 0:
    print("X e Y devem ser valores inteiros positivos.")
else:
   
    resultado = x ** y

    print(f"{x}^{y} = {resultado}")
