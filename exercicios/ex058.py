from random import randint
tent = 1
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
pc = randint(0, 10)
n = int(input('Qual é o seu palpite? '))

while n != pc:
    tent += 1
    
    if n < pc:
        print('Mais... Tente mais uma vez.')
        n = int(input('Qual é o seu palpite? '))
    else:
        print('Menos... Tente mais uma vez.')
        n = int(input('Qual é o seu palpite? '))

print(f'Acertou com {tent} tentativas. Parabéns!')