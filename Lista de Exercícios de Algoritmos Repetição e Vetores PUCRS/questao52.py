
N = int(input("Digite o valor de N (tamanho do conjunto): "))
p = int(input("Digite o valor de p (tamanho dos subconjuntos): "))


combinacao = 1
arranjo = 1


for i in range(p):
    combinacao *= N - i
    combinacao //= i + 1


for i in range(p):
    arranjo *= N - i


print(f"Combinação ({N} choose {p}): {combinacao}")
print(f"Arranjo ({N} P {p}): {arranjo}")
