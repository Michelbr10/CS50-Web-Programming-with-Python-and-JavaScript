#criar uma classe para verificar assentos em voo
class Voo:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.passageiros = []
        
    def add_passageiro(self, nome):
        if not self.assentos(): #se a capacidade for igual a 0, a condição será false
            return False
        self.passageiros.append(nome)
        return True
    
    def assentos(self):
        return self.capacidade - len(self.passageiros)


voo = Voo(3)
print(f'Capacidade: {voo.capacidade}, Passageiros: {len(voo.passageiros)}')

pessoas = ['Micthel', 'Ana', 'Bukowski', 'Henry']

for pessoa in pessoas:
    if voo.add_passageiro(pessoa):
        print(f'O passageiro {pessoa} foi adicionado ao voo.')
    else:
        print(f'Não há assentos disponíveis para {pessoa}!')
        
    print(f'Capacidade: {voo.capacidade}, Passageiros: {len(voo.passageiros)}')