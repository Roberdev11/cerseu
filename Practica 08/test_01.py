"""
    Manejo de archivos
"""

"""
    r: Abre el archivo en modo de lectura
"""

file = open("my_files/example.txt", "r")

"""
    read(): Nos permite leer el contenido de un archivo
"""

print("El contenido de nuestro archivo 'example.txt': {}".format(file.read()))

file.close()
