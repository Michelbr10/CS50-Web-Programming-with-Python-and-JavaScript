pessoas = [
    {'nome': 'Mitchel', 'idade':'23'},
    {'nome': 'Ana', 'idade':'45'},
    {'nome': 'Bukowski', 'idade':'60'}
]

# def classifica(pessoa):
#     return pessoa['nome']

#a função lambda é equivalente a uma função normal
pessoas.sort(key=lambda pessoa: pessoa['nome'])

print(pessoas)