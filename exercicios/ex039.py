import datetime
ano = int(input('Ano de nascimento: '))
atual = datetime.datetime.now().year

idade = atual - ano
alis = 18 - idade

print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')

if idade < 18:
    print(f'Ainda faltam {alis} ano(s) para o alistamento.')
    print(f'Seu alistamento será em {atual + alis}')
    
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos')
    print(f'Seu alistamento foi em {atual - (idade - 18)}')
    
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
