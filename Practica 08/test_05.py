"""
    Manejo de archivos
"""

tecnologiasBackend = ["\n-Python", "\n-Java", "\n-Ruby", "\n-NodeJS"]

file = open("my_files/example_05.txt", "a+")
file.writelines(tecnologiasBackend)

file = open("my_files/example_05.txt", "r")

for newLline in file:
    #print(newLline)
    if newLline.find("Python"):
        print("Tienes en tu lista a Python")
    else:
        print("No existe en tu lista")

file.close()
