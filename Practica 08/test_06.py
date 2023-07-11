
"""Manejo de archivos"""


def fileManipulation(dir, mode):
    try:
        file = open(dir, mode)
        print(file.read())
        file.close()
        return file
    except OSError as err:
        print("Error de lectura: {}: ".format(err))

fileWrite = "my_files/example_02.txt"

print("Lectura de archivo")
fileManipulation(fileWrite, "r")

fileWrite2 = "my_files/example_08.txt"
fileManipulation(fileWrite2, "a+")
