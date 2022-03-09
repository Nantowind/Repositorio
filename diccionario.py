diccionario = {"c1": "valor1", "c2": "valor2"}
print(diccionario)
resultado = diccionario["c1"]
print(resultado)

cliente = {"nombre": "Juan", "apellido": "Fuentes", "Peso": 65, "talla": 1.75}

consulta = cliente["Peso"]
print(consulta)

dic = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'sc1': 100, 'sc2': 100, 'sc3': 300}}
print('\n', dic['c2'][0:3], "  ", dic['c3']['sc1'])

dicci = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f'], 'c3': 'X'}
dicci['c4'] = "z"
dicci[45] = "numero"
dicci['c1'] = dicci['c1'][0].upper() + dicci['c2'][0].upper()

print(dicci['c2'][1].upper(), dicci['c4'].upper(), dicci[45], dicci['c1'])

print('\n', dicci.keys())

print('\n', dicci.values())

print('\n', dicci.items())

