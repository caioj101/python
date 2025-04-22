casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
ano = int(input('Quantos anos de financioamento? '))

prestacao = casa / (ano * 12)
minimo = (salario * 30) / 100

print(f'Para pagar uma casa de R${salario:.2f} em {ano} anos a prestação será de R${prestacao:.2f}')

if prestacao >= minimo:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
