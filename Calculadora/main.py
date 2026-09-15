# ACTIVIDAD PRINCIPAL

numero1 = int(input())
numero2 = int(input())

resultado = numero1 + numero2
print(resultado)


# ACTIVIDADES EXTRA

print("\n--- ACTIVIDADES EXTRA ---")

print("Resta:", numero1 - numero2)
print("Multiplicación:", numero1 * numero2)

if numero2 != 0:
    print("División:", numero1 / numero2)
    print("Módulo:", numero1 % numero2)
else:
    print("No se puede dividir entre 0")
    print("No se puede calcular el módulo entre 0")


# ELEGIR UNA OPERACIÓN

print("\n¿Qué operación quieres realizar?")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Módulo")

opcion = input("Elige una opción del 1 al 5: ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == "1":
    print("Resultado:", num1 + num2)

elif opcion == "2":
    print("Resultado:", num1 - num2)

elif opcion == "3":
    print("Resultado:", num1 * num2)

elif opcion == "4":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("No se puede dividir entre 0")

elif opcion == "5":
    if num2 != 0:
        print("Resultado:", num1 % num2)
    else:
        print("No se puede calcular el módulo entre 0")

else:
    print("Opción no válida")


# SUMAR TRES NÚMEROS

print("\n--- SUMA DE TRES NÚMEROS ---")

n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
n3 = float(input("Ingresa el tercer número: "))

suma3 = n1 + n2 + n3

print("La suma de los tres números es:", suma3)


# MEZCLAR OPERACIONES CON 3 NÚMEROS O MÁS

print("\n--- OPERACIONES COMBINADAS ---")

cantidad = int(input("¿Cuántos números quieres utilizar? "))

if cantidad < 3:
    print("Debes utilizar al menos 3 números.")

else:
    numeros = []
    operadores = []

    for i in range(cantidad):
        numero = float(
            input("Ingresa el número " + str(i + 1) + ": ")
        )
        numeros.append(numero)

        if i < cantidad - 1:
            operador = input(
                "Ingresa una operación (+, -, *, /, %): "
            )

            while operador not in ["+", "-", "*", "/", "%"]:
                print("Operación no válida.")
                operador = input(
                    "Ingresa una operación (+, -, *, /, %): "
                )

            operadores.append(operador)

    error = False
    i = 0

    # Primero multiplicación, división y módulo
    while i < len(operadores):

        if operadores[i] == "*":
            numeros[i] = numeros[i] * numeros[i + 1]

            del numeros[i + 1]
            del operadores[i]

        elif operadores[i] == "/":
            if numeros[i + 1] == 0:
                print("No se puede dividir entre 0")
                error = True
                break

            numeros[i] = numeros[i] / numeros[i + 1]

            del numeros[i + 1]
            del operadores[i]

        elif operadores[i] == "%":
            if numeros[i + 1] == 0:
                print("No se puede calcular el módulo entre 0")
                error = True
                break

            numeros[i] = numeros[i] % numeros[i + 1]

            del numeros[i + 1]
            del operadores[i]

        else:
            i += 1

    # Después suma y resta
    if not error:
        resultado_final = numeros[0]

        for i in range(len(operadores)):

            if operadores[i] == "+":
                resultado_final = resultado_final + numeros[i + 1]

            elif operadores[i] == "-":
                resultado_final = resultado_final - numeros[i + 1]

        print("Resultado de las operaciones combinadas:", resultado_final)