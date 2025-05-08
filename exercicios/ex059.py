from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5 ] sair do programa''')
opcao = int(input('>>>>> Qual é a sua opção? '))

while opcao != 5:
    if opcao == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}')
        print('=-=' * 10)
        sleep(1)
        
    elif opcao == 2:
        print(f'A multiplicação entre {n1} * {n2} é {n1*n2}')
        print('=-=' * 10)
        sleep(1)
        
    elif opcao == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor é {n1}')
            print('=-=' * 10)
            sleep(1)
            
        elif n1 < n2:
            print(f'Entre {n1} e {n2} o maior valor é {n2}')
            print('=-=' * 10)
            sleep(1)
            
        else:
            print('Os valores são iguais!')
            print('=-=' * 10)
            sleep(1)
            
        
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        
    else:
        print('Opção inválida. Tente novamente,')
        sleep(1)
    
    
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))       

print('Obrigado e volte sempre!')
