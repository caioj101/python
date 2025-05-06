print("========== LOJAS CARDOSO ==========")
preco = float(input('Preço das compras: R$'))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")

opcao = int(input('Qual é a sua opção? '))

if opcao == 1:
    desconto = preco - (preco * 10 / 100)
    print(f'Sua compra de R${preco:.2f} vai custar R${desconto:.2f} no final ')
    
elif opcao == 2:
    desconto = preco - (preco * 5 / 100)
    print(f'Sua compra de R${preco:.2f} vai custar R${desconto:.2f} no final ')
    
elif opcao == 3:
    print(f'Sua compra será parcelada em 2x de R${preco / 2:.2f} SEM JUROS')
    
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    aumento = preco + (preco * 20 / 100)
    print(f'Sua compra será parcelada em {parcela}x de R${aumento / parcela:.2f} COM JUROS')
    print(f'Sua compra de R${preco:.2f} vai custar R${aumento:.2f} no final')
    
else:
    print('OPÇÃO INVÁLIDA!')
