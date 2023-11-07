import random

grupos = []


for ind_grupo in range(5):
    grupo = []
    for input_numero in range(4):
        # numero = int(input(f"Digite o numero que estará na pos {input_numero+1} para o grupo {ind_grupo+1}: "))
        # Inserindo valores aleatórios para teste
        numero  = random.randint(0, 15)
        grupo.append(numero)
    grupos.append(grupo)

for grupo in grupos:
    ind = 1
    ordem_crescente = sorted(grupo)
    # ordena o vetor em forma decrescente
    ordem_decrescente = sorted(grupo, reverse=True) 
    print(f"Grupo {ind}")
    print(f"Na ordem normal: {grupo}")
    print(f"\tNa ordem crescente: {ordem_crescente}")
    list(grupo).sort(reverse=True)
    print(f"\tNa ordem descrecente: {ordem_decrescente}")
    ind+=1