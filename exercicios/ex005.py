from cores import colorir

print(f'{colorir("ANTECESSOR E SUCESSOR >>>>>>>>>>", cor="verde", estilo="negrito")}')


n = int(input('Digite um número: '))
print(f'Analisando o valor {colorir(n, cor="magenta", estilo="negrito")}, seu antecessor é {colorir(n-1, cor="vermelho", estilo="negrito")} e o sucessor é {colorir(n+1, cor="verde", estilo="negrito")}')
