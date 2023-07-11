"""Listas en Python"""

"""Listas (insert): Insertar elementos en una posición dada"""

lista = [10, 50, 80, 22, 100]

lista.insert(1, 200)

print("El valor de mi lista actualizada es: {}".format(lista))

"""Insertar valor 'Hola Pythonista' al final de la lista"""
lista.insert(len(lista), "Hola Pythonista")

print("El valor de mi lista actualizada es: {}".format(lista))
