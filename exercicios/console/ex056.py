total = 0
mulher = 0
velho = 0
for c in range(1, 5):
    print(f'----- {c}° PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    total += idade
    if sexo == 'F' and idade < 20:
        mulher += 1
    if sexo == 'M':
        if idade > velho:
            velho = idade
            nomevelho = nome

media = total / 4

print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {velho} e se chama {nomevelho}')
print(f'Ao todo são {mulher} mulheres com menos de 20 anos')
