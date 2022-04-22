idades = [39, 30, 27, 18]
print(type(idades))

idades.append(15)

idades.append(27)
print(idades)

# remove a primeira aparicao do item
idades.remove(27)
print(idades)

if 15 in idades:
    idades.remove(15)

idades.insert(0, 20)
print(idades)

idades.extend([27, 19])
print(idades)

# list comprehension
print([idade for idade in idades if idade > 21])

def proximo_ano(idade):
    return idade + 1

print([proximo_ano(idade) for idade in idades if idade > 21])


def faz(lista = None):
    print('Cria sempre uma lista nova.')
    if lista == None:
        lista = list()
    print(len(lista))
    lista.append(1)
    print(lista)

def faz2(lista = []):
    print('Inicializa lista vazia, que sera referenciada na memoria')
    print(len(lista))
    lista.append(1)
    print(lista)