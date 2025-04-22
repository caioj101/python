print('-=' * 15)
print('Analisador de Triâgulos')
print('-=' * 15)
segmento1 = float(input('Primeiro segmento: '))
segmento2 = float(input('Segundo segmento: '))
segmento3 = float(input('Terceiro segmento: '))

if segmento1 + segmento2 > segmento3 and segmento2 + segmento3 > segmento1 and segmento1 + segmento3 > segmento2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')