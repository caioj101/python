peso = float(input('Qual o seu peso? (kg) '))
alt = float(input('Qual é a sua altura? (m) '))

imc = peso / (alt * alt)

print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
    
elif imc <= 25:
    print('PARABÉNS. você está na faixa de PESO NORMAL!')
    
elif imc < 30:
    print('Você está em SOBREPESO!')
    
elif imc < 40:
    print('Você está em OBESIDADE!')
    
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
