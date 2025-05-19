from time import sleep
from random import choice

print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
opcao = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']

pc = choice(jokenpo)
jogador = jokenpo[opcao]

print('-=' * 10)
print(f'Computador jogou {pc}')
if opcao == 0:
    print('Jogador jogou PEDRA')
    
elif opcao == 1:
    print('Jogador jogou PAPEL')
    
elif opcao == 2:
    print('Jogador jogou TESOURA')
print('-=' * 10)

if jogador == 'PEDRA' and pc == 'PAPEL' or jogador == 'PAPEL' and pc == 'TESOURA' or jogador == 'TESOURA' and pc == 'PEDRA':
    print('PC VENCE')
elif jogador == 'PEDRA' and pc == 'TESOURA' or jogador == 'PAPEL'  and pc == 'PEDRA' or jogador == 'TESOURA' and pc == 'PAPEL':
    print('JOGADOR VENCE')
else:
    print('EMPATE')
