cont = soma = 0

while True:
    n = int(input('Digite um valor(999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} foi {soma}!')

# A ordem dos contadores é importante, sempre depois da flag a ser verificada pra não ser contabilizada
