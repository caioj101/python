primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
total_termos = 10
contado_ja = 0
p = 1

while p != 0:
    while contado_ja < total_termos:
        atual = primeiro + (contado_ja) * razao
        print(f'{atual}', end=' -> ')
        contado_ja +=1
    print('Pausa', end='')
    
    p = int(input('\nQuantos termos você quer mostrar agora? '))
    total_termos += p
    
print(f'Progressao finalizada com {contado_ja} termos mostrados')
