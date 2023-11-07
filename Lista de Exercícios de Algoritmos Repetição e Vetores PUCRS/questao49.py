
n = int(input("Digite um valor N inteiro e positivo: "))


if n < 0:
    print("N deve ser um valor inteiro positivo.")
else:
 
    fatorial = 1

 
    for i in range(1, n + 1):
        fatorial *= i

   
    print(f"{n}! = {fatorial}")

