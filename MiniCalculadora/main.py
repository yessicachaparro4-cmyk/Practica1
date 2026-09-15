def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir entre 0"


print(sumar(8, 2))
print(restar(8, 2))
print(multiplicar(8, 2))
print(dividir(8, 2))


def potencia(base, exponente):
    return base ** exponente


print(potencia(2, 3))
