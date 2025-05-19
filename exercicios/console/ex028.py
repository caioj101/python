from random import randint 
from time import sleep
print('-=--' * 15)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=--' * 15)
r = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
pc = randint(0, 5)
if r == pc:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {pc} e não no {r}')
    