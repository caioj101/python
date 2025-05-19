valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    while resp not in ['s', 'n']:
        print('Dado inválido. Tente novamente! ', end='')
        resp = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    if resp == 'n':
        break
 
valores.sort(reverse=True)

print('-=' * 20)
print(f'Você digitou {len(valores)} elementos')
print(f'Os valores em ordem descrescente são {valores}' )
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista')
