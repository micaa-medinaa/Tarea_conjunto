
"""
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

mayor = num1 if num1 > num2 else num2

print(f"El número mayor es: {mayor}")

"""
"""
def buscar_palabra(palabra_buscada, *args):
   
    resultado = "¡Encontrada!" if palabra_buscada in args else "No encontrada."
    return resultado


entrada_palabras = input("Ingresa varias palabras separadas por espacio: ").split()


palabra_a_buscar = input("¿Qué palabra deseas buscar?: ")

# 3. Llamamos a la función usando * para pasar la lista como *args
mensaje = buscar_palabra(palabra_a_buscar, *entrada_palabras)

# 4. Mostramos el resultado usando un f-string
print(f"Resultado: La palabra '{palabra_a_buscar}' fue {mensaje}")

"""
"""
num1 = int(input("Ingresa un número: "))

resultado = "Par" if num1 % 2 == 0 else "Impar"

print(f"El número es: {resultado}")

"""

"""
def calcular_promedio(*args):
  
    return sum(args) / len(args) if len(args) > 0 else 0


entrada = input("Ingresa varios números separados por espacio (ej: 10 20 30): ")


lista_numeros = [float(num) for num in entrada.split()]


resultado = calcular_promedio(*lista_numeros)


print(f"El promedio de los números ingresados es: {resultado}")

"""

def validar_argumentos(*args):
   
    return "Error: Faltan argumentos (necesitas al menos 2)." if len(args) < 2 else f"¡Todo en orden! Procesando {len(args)} elementos..."


entrada = input("Ingresa al menos 2 números separados por espacio: ")
lista = entrada.split()


resultado = validar_argumentos(*lista)
print(resultado)

