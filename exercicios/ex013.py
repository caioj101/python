salario = float(input('Qual é o salário do Funcionário? R$'))
novosalario = salario + (salario * 15 / 100)
print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${novosalario:.2f}')
