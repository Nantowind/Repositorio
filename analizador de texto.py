print("""Hola esto es un analizador de texto en el analizalemos el terxto ingresado y te daremos varios datos sobre el.
Para eso necesitamos que ingreses una oracion como una frase, un poema, etc.""")

# Aqui pedimos el texto y lo pasasmos a minuscula
texto = input("Ingrese su texto: ")
texto = texto.lower()

# Aqui pedimos las letras a analizar y las pasamos a minuscula
print("Ahora vamos a necesitar que ingrese 3 letras, numeros o palabras enteras")
lista_letras = [input("\ningreso 1: "), input("\ningreso 2: "), input("\ningreso 3: ")]
lista_letras[0], lista_letras[1], lista_letras[2] = lista_letras[0].lower(), lista_letras[1].lower(), lista_letras[2].lower()

# Aqui hacemos el conteo de letras y palabras de que nos ingresaron
tupla_conteo = (texto.count(lista_letras[0]), texto.count(lista_letras[1]), texto.count(lista_letras[2]))
print("La letra/numero/palabra:", lista_letras[0], "aparece: ", tupla_conteo[0], "veces.")
print("La letra/numero/palabra:", lista_letras[1], "aparece: ", tupla_conteo[1], "veces.")
print("La letra/numero/palabra:", lista_letras[2], "aparece: ", tupla_conteo[2], "veces.")

# Aqui vamos a convertir el texto a una lista para hacer su conteo
texto2 = texto.split()
print("Tiene:", len(texto2), "palabras.")

# Aqui vamos a mostrar la primera y ultima letra de el texto
print("Empieza con", texto[:1], "y termina con: ", texto[-1:])

# Aqui vamos a poner la lista que armamos con el texto en reversa y agregar espacios
texto2.reverse()
lista_volteada = " ".join(texto2)
print("A si se veria tu texto escrito al revez \n ", lista_volteada)

# Ahora vamos a ver si python se encuentra en el texto con un diccionario
python_bool = {True: "Python esta en el texto", False: "Python no esta en el Texto"}

print("la palabra ", python_bool["python" in texto])