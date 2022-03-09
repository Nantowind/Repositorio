texto = "ESTE ES EL TEXTO DE FEDERICO"
x = " "

resultado = texto.split(x)

print(resultado)

a, b, c, d, f = "aprender", "python", "es", "genial", "aprender"
e = " ".join([a, b, c, d, f])
print(e)

resultado = texto.find("S")
print(resultado)
resultado = texto.index("T")
print(resultado)
e = e.replace("aprender", "remplazado")
print(e)

palabras = "palabra1, palabra2."

resultado = palabras.replace("palabra1", "remplazo1")


print(resultado)

resultado = palabras.replace("palabra2", "remplazo2")

print(resultado)