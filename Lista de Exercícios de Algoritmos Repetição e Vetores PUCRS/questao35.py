maior_altura = -1
menor_altura = 999
media_geral = 0
media_altura_mulheres = 0
contador_mulheres = 0
contador = 0

for i in range (3):
    altura = float(input("Digite aqui a altura em cm ->  "))
    sexo = input("1 para masculino - 2 para feminino -> ")
    media_geral += altura
    contador+= 1

    if altura < menor_altura: 
        menor_altura = altura
    if altura > maior_altura:
        maior_altura = altura

    if sexo == '2':
        media_altura_mulheres += altura
        contador_mulheres += 1

media_altura_mulheres = media_altura_mulheres/contador_mulheres
media_geral = media_geral/contador

print(f"\nA maior altura foi de {maior_altura:.2f}\nA menor altura foi de {menor_altura:.2f}\nA media de altura das mulheres foi de {media_altura_mulheres:.2f}\nA media de altura da turma foi de {media_geral:.2f}")
    
