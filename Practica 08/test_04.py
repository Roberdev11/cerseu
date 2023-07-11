"""
    Manejo de archivos
"""

titulo1 = "Tecnologias Backend: "
tecnologiasBackend = ["\n-Python", "\n-Java", "\n-Ruby", "\n-NodeJS"]

#tecnologiasBackend[0] = titulo1

file = open("my_files/example_04.txt", "a+")

file.writelines(titulo1)
file.writelines(tecnologiasBackend)

file = open("my_files/example_04.txt", "r")
print(file.read())

"""Cierre de archivos"""
file.close()
