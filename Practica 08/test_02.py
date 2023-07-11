"""
    Manejo de archivos
"""
"""
    w: Abre el archivo para poder escribir sobre el
"""

file = open("my_files/example_02.txt", "w")

file.write("\nCaracterpisticas en Python:\n")
file.write("* Lenguaje multiplataforma\n")
file.write("* Basado en POO\n")
file.write("* Python es un lenguaje intuitivo")

file = open("my_files/example_02.txt", "r")
print("Contenido del archivo example_02.txt: {}".format(file.read()))

"""Cierre del archivo"""
file.close()
