from cores import colorir

print(f'{colorir("CONVERSOR DE MOEDAS >>>>>>>>>>", cor="verde", estilo="negrito")}')

br = float(input('Quanto dinheiro você tem na carteira? R$'))
us = br / 5.66 #cotação da época né
print(f'Com R${colorir(f"{br:.2f}", cor="magenta", estilo="negrito")} você pode comprar US${colorir(f"{us:.2f}", cor="verde", estilo="negrito")}')
