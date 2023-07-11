"""Listas en Python"""

"""Listas (pop()): Quita un elemento de una posición existente de la lista"""

paises = ["Perú", "España", "Brasil", "Colombia"]

print("Mi lista inicial es la siguiente: {}".format(paises))

paises.pop()

print("Mi lista actualizada es la siguiente: {}".format(paises))

"""Está eliminando el valor del país de España"""
paises.pop(2)

print("Mi lista actualizada es la siguiente: {}".format(paises))

paises.pop(1)
print("Mi lista actualizada es la siguiente: {}".format(paises))

