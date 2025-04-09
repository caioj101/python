import math

ang = float(input('Digite o ângulo que você deseja: '))
rad = math.radians(ang)
print(f'O ângulo de {ang} tem SENO de {math.sin(rad):.2f}')
print(f'O ângulo de {ang} tem COSSENO de {math.cos(rad):.2f}')
print(f'O ângulo de {ang} tem TANGENTE de {math.tan(rad):.2f}')
