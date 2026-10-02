"""
print ("Vamos a realizar una división")

try:
    num1 = float(input("Ingresá el primer número: "))
    num2 = float(input("Ingresá el segundo número: "))

    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.") #Capturamos el error debido a que no se puede dividir por 0
    
else:
    print("Sin errores")

"""

"""
try:
    num1 = float(input("Ingresá el primer número: "))
    num2 = float(input("Ingresá el segundo número: "))


    resultado = num1 + str(num2)
    print(f"El resultado de la suma es: {resultado}")

except TypeError:
    print("Error: No se puede sumar un número con una cadena de texto.")

else:
    print("Operación realizada sin errores.")

"""
"""
usuario = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Mendoza"
}

try:
    telefono = usuario["telefono"]
    print(f"El teléfono es: {telefono}")

except KeyError:
    print("Error: La clave buscada no existe en el diccionario.")

else:
    print("Clave encontrada con éxito.")

"""

"""
nombre_archivo = "mi_archivo.txt"
archivo_existe = True

try:
    with open(nombre_archivo, "r") as archivo:
        print(archivo.read())

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe.")
    archivo_existe = False

finally:
    if not archivo_existe:
        with open(nombre_archivo, "w") as archivo_nuevo:
            archivo_nuevo.write("Archivo creado desde el bloque finally.")
        print("Archivo creado correctamente.")

"""

print("Vamos a realizar una división de dos números")

try:
    num1 = float(input("Ingresá el primer número (dividendo): "))
    num2 = float(input("Ingresá el segundo número (divisor): "))

    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")

except ValueError:
    print("Error: Ingresaste un valor no válido, ingrese un número.")

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

else:
    print("La operación se completó con éxito.")




