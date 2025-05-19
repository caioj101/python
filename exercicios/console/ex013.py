from cores import colorir

print(f'{colorir("REAJUSTE SALARIAL >>>>>>>>>>", cor="verde", estilo="negrito")}')

salario = float(input('Qual é o salário do Funcionário? R$'))
novosalario = salario + (salario * 15 / 100)
print(f'Um funcionário que ganhava R${colorir(f"{salario:.2f}", cor="magenta", estilo="negrito")}, com 15% de aumento, passa a receber R${colorir(f"{novosalario:.2f}", cor="verde", estilo="negrito")}')
