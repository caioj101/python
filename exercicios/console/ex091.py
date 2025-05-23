from random import randint
from operator import itemgetter
from time import sleep

valores = {}
jogador = []

print('Valores sorteados:')
sleep(1)

for j in range(1, 5):
    dado = randint(1, 6)
    print(f'Jogador{j} tirou {dado} no dado')
    sleep(1)
    valores['jogador'] = j
    valores['numero'] = dado
    jogador.append(valores.copy())
    
ordenado = sorted(jogador, key=itemgetter('numero'), reverse=True)

print('  == RANKING DOS JOGADORES ==  ')
for i, e in enumerate(ordenado, start=1):
    print(f'  {i}° lugar: Jogador{e["jogador"]} com {e["numero"]}')
    sleep(1)