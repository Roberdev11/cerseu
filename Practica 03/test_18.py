"""Diccionarios en Python"""

varDiccionario = {"nombre": "Mysql", "tipo": "BD Relacional"}

"""Obteniendo solamente los valores de los keys o columnas"""

keys = sorted(varDiccionario)
print(keys)

valores = list(varDiccionario.values())
print(valores)

keys_2 = list(varDiccionario.keys())
print(keys_2)

"""Convirtiendo el diccionario a una lista"""
lista_convertida = varDiccionario.items()
print(lista_convertida)
