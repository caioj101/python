seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg1 + seg3 > seg2:
    if seg1 == seg2 == seg3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
    elif seg1 != seg2 != seg3 and seg1 != seg3 != seg2 :
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
    else:
        print('Os segmentos acima podem formar um triângulo ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')
