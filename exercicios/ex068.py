from random import randint
soma = cont = 0

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

while True:
    pc = randint(0, 10)
    n = int(input('Digite um valor: '))
    opcao = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    while 'I' not in opcao and 'P' not in opcao:
        print('Opção inválida. Tente novamente')
        opcao = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('-' * 25)
    soma = n + pc
    print(f'Você jogou {n} e o computador {pc}. Total de {soma}. ', end='', )    
    if soma % 2 == 0:
        print('DEU PAR')
        if opcao == 'P':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-' * 15)
            cont += 1
        else:
            print('Você PERDEU!')
            print('=-' * 15)
            break           
    else:
        print('DEU ÍMPAR')
        if opcao == 'I':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-' * 15)
            cont += 1
        else:
            print('Você PERDEU!!')
            print('=-' * 15)
            break 
print(f'GAME OVER! Você venceu {cont} vezes.')
