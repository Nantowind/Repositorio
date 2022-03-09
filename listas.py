mi_lista = ['a', 'b', 'c']

otra_lista = ['hola', 25, bool, len(mi_lista), float]
resultado = mi_lista[0:2]
print(otra_lista)
print(resultado)
print(mi_lista + otra_lista)
mi_lista[0] = "alfa"
print(mi_lista)
mi_lista.append("lomega")
eliminado = mi_lista.pop(0)
print(mi_lista)
print(eliminado)

lista = ['a', 'c', 'y', 'm']
lista.sort()
lista2 = lista
print(lista)
print(lista2)
lista.reverse()
print(lista)