'''
decoradores em python servem para adicionarmos algo a mais em uma função,
é uma função que recebe uma outra função como entrada e retorna uma versão
modificada dessa função como saída.
'''

def anunciar(f):
    def exibe():
        print('Estamos executando a função')
        f()
        print('Execução concluída')
    return exibe

@anunciar
def hello():
    print('Olá, mundo!')

hello()
