import random

# Lista de nombres de ejemplo
nombres_originales = ["Juan", "María", "Luis", "Ana", "Carlos"]

# Seleccionar un número determinado de nombres aleatorios
num_nombres_a_seleccionar = 1
nombres_seleccionados = random.sample(nombres_originales, num_nombres_a_seleccionar)

# Unir los nombres seleccionados en una cadena usando ', '
nombres_seleccionados_str = ', '.join(nombres_seleccionados)

# Aquí podrías almacenar los nombres seleccionados en otra tabla o estructura de datos, según tus necesidades.

print("Nombres seleccionados:", nombres_seleccionados_str)
