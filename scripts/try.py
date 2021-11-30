lista = []
a = 10
b = 20
def teste():
    lista.append([a, b])
    return lista
lista = teste()
print(lista[0])