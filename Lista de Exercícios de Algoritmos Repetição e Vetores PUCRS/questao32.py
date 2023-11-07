for i in range (5):
    a = int(input("Digite um valor INTEIRO E POSITIVO qualquer ->  "))
    b = int(input("Digite um valor INTEIRO E POSITIVO qualquer ->  "))
    if a < b:
        for i in range(a, b + 1):
            if i % 2 == 0:
                print(i)
            