import sys

try:
    a = float(input('Insira o divisor: '))
    b = float(input('Insira um dividendo: '))
except ValueError:
    print('Erro: valor inválido.')
    sys.exit(1)

try:
    resultado = a / b
except ZeroDivisionError:
    print('Erro: não pode dividir por zero.')
    sys.exit(1)

print(f'O número {a} dividido por {b} é {resultado}')
