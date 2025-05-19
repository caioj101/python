from cores import colorir

print(f'{colorir('SOMANDO DOIS NUMEROS >>>>>>>>>>', cor="verde", estilo="negrito")}')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print(f'A soma entre {colorir(n1, cor="vermelho")} e {colorir(n2, cor="vermelho")} é igual a  {colorir(n1+n2, cor="verde")}!')
