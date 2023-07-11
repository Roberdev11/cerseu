"""
    Manejo de archivos
"""

tecnologiasBackend = ["Python", "Java", "NodeJS\n"]
tecnologiasFrontend = ["Angular", "React JS", "Boostrap"]

"""
    Apertura de nuestro archiv:
    a+: Permite escribir varias líneas en nuestro archivo
    a+: Escribe nuevas líneas de texto sin sobreescribir el contenido del archivo
"""

file = open("my_files/example_03.txt", "a+")

file.writelines(tecnologiasBackend)
file.writelines(tecnologiasFrontend)

file = open("my_files/example_03.txt", "r")

print("El contenido de mi archivo file_3.txt es: {}".format(file.read()))
file.close()
