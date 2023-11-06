n = int(input("Digite o número de termos (n) da progressão aritmética: "))
a1 = float(input("Digite o primeiro termo (a1) da progressão aritmética: "))
r = float(input("Digite a razão (r) da progressão aritmética: "))

termos = [] 

for i in range(n):
    termo = a1 + i * r 
    termos.append(termo) 


print(f"Os {n} termos da progressão aritmética são:")
soma = 0
for termo in termos:
    print(termo)
    soma += termo


print(f"\nA soma dos {n} termos da progressão aritmética é: {soma}")
