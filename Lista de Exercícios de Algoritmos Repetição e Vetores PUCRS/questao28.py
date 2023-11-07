valor = 0
s = 0
valor = int(input("Digite aqui um numero inteiro e positivo ->  "))
if valor <= 0:
    print("Digite um valor valido.... ")
else:   
    
    for i in range (1,valor+1):
        s += 1/i
        print(f"\n{s}")
        
    
print(f"\nA Soma final foi de -> {s:.3f}")