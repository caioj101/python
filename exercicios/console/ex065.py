resp = 'S'
vezes = 0
total = 0
maior = 0
menor = 0
while  resp == 'S':
    n = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if resp != 'N' and resp != 'S':
        print('Solicitação inválida. Tente novamente!')
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
    vezes += 1
    total += n
    if vezes == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n        
media = total / vezes
print(f'Você digitou {vezes} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
