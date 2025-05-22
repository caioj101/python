from random import sample
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^5}')
print('-' * 30)

jogos = int(input('Quantos jogos você quer que sorteie? '))

print(f'-=-=-= SORTEANDO {jogos} JOGOS -=-=-=')

for c in range(1, jogos+1):
    aleatorio = sample(range(1, 60), k=6)
    print(f'Jogo {c}: {sorted(aleatorio)}')
print('-=-=-=-=-= < BOA SORTE > -=-=-=-=-=')