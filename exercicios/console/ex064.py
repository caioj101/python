total = 0
cont = 0
n = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        cont += 1
        total += n
print(f'Você digitou {cont} números e a soma entre eles foi {total}.')