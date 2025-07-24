# Programa para calcular el promedio de una lista de n�meros

print("Bienvenido al programa de c�lculo de promedios.")
print("Ingresa n�meros uno por uno. Escribe 'salir' para terminar.")

# Lista para almacenar los n�meros
numeros = []

while True:
    entrada = input("Ingresa un n�mero (o escribe 'salir'): ")
    
    if entrada.lower() == 'salir':
        break  # Salir del bucle si el usuario escribe 'salir'
    
    try:
        # Convertir la entrada a n�mero
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, ingresa un n�mero v�lido.")
        continue

# Verificar si hay n�meros en la lista antes de calcular el promedio
if len(numeros) > 0:
    promedio = sum(numeros) / len(numeros)
    print(f"El promedio de los n�meros ingresados es: {promedio:.2f}")
else:
    print("No ingresaste ning�n n�mero.")

