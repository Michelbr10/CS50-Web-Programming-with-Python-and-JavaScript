#criar um conjunto vazio
conjunto_vazio = set() #set é uma coleção não ordenada de elementos únicos.

#adiconando elementos ao conjunto_vazio
conjunto_vazio.add(1)
conjunto_vazio.add(2)
conjunto_vazio.add(3)
conjunto_vazio.add(4)
conjunto_vazio.add(3)
conjunto_vazio.add(2)
print(conjunto_vazio) #mesmo adiconando elementos repetidos, os elementos aparecem apenas uma vez

conjunto_vazio.remove(2) #para remover elementos usa-se .remove

print(conjunto_vazio)
print(f'O conjunto possui {len(conjunto_vazio)} elementos.')