total = milacima = 0
menorprod = ''
prod_cadastrados = 1

print('-' * 30)
print('     LOJAS SUPER BARATÃO')
print('-' * 30)

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    
    total += preco
    
    if preco > 1000:
        milacima += 1
    
    if prod_cadastrados == 1:
        menor = preco
        menorprod = produto
    else:
        if preco < menor:
            menor = preco
            menorprod = produto
    
    prod_cadastrados += 1
            
    print('-' * 30)
    print('Produto cadastrado com sucesso!')
    print('-' * 30)
    
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in ['S', 'N']:
        print('Opção Inválida. Tente novamente.')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    if resp == 'N':
        break
    
print('---------- FIM DO PROGRAMA ----------')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {milacima} produto(s) custando mais de R$1000.00')
print((f'O produto mais barato foi {menorprod} que custa R${menor:.2f}'))
