def decorador(func):
    def retorno(*args, **kwargs):
        valor_retorno = func(*args, **kwargs)
        print(*args, **kwargs)
        return valor_retorno
    return retorno


@decorador
def soma(a, b, c):
    return a + b + c

print(soma(5, 3, 2))
