maior = homem = menormulher = 0

while True:
    print('-' * 30)
    print('    CADASTRE UMA PESSOA   ')
    print('-' * 30)
    
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in ['M', 'F']:
        print('Opção Inválida. Tente novamente.')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]   
    print('-' * 30)
    
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        menormulher += 1
          
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in ['S', 'N']:
        print('Opção Inválida. Tente novamente.')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {menormulher} mulheres com menos de 20 anos')
