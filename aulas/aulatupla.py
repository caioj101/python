#ANOTAÇÕES DESSA AULA

#Usamos () pra Tuplas, [] pra Lista e {} para um Dicionário
# 3 Formas de fazer a mesma coisa, mas de um jeito diferente.
lanche =('Hambúrguer', 'suco', 'pizza', 'pudim', 'pão')#Variávem com mais espaços
for cont in range(0, len(lanche)):#Mostrando a posição dos Obj na Variável usando o RANGE
    print(f'eu vou comer {lanche[cont]} na posição {cont}')
for pos, comida in enumerate (lanche): #Mostrando a posição dos Obj usando o ENUMERATE
    print(f'Eu vou comer {comida} na posição {pos}')
for comida in lanche:
    print(f'Eu vou comer {comida}')#Não precisa mostrar a Posição do Obj na Variável
print('comi pra carai')
print(sorted(lanche)) #Sorted serve pra organizar a Variável
#fazendo tuplas com números
a=(2,5,8)
b=(1,6,8,9)
c=a+b
print(c)
print(c.count(8))#contar quantas vezes apareceu o número na tupla
print(c.index(5))#mostrar a posição do número 5 na Tupla


