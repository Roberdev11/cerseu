"""Listas en Python"""

"""Listas (count): Cantidad de veces que aparece un elemento que se repite en una lista"""

list_1 = ["Python", "Java", "PHP", "Ruby", "Java", "Javascript", "Java", "Typescript", "Java"]

list_1.append("Python")
list_1.append("Python")

print("Mi lista actualizada tiene los siguiente valores: {}".format(list_1))
print("Cantidad de veces que aparece 'Java' es {}".format(list_1.count("Java")))
print("Cantidad de veces que aparece 'Python' es {}".format(list_1.count("Python")))
