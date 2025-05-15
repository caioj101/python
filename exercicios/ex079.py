valores = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Não vou adicionar')
        
    resp = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
    while resp not in ['s', 'n']:
        print('Dado inválido. Tente novamente. ', end='' )
        resp = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
        
    if resp == 'n':
        break

print('-=' * 20)
print(f'Você digitou os valores {valores.sort()}')
