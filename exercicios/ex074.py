numeros = ()
from random import randint

for c in range (0,5):
    n = randint (0,10)
    numeros = numeros + (n,)


print(f'Os valores sorteados foram: ', *numeros, sep=' ')
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
