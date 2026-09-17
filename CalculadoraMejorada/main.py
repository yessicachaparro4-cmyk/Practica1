def addmultiplenumbers(numbers):
    return sum(numbers)


def multiplymultiplenumbers(numbers):
    resultado = 1
    for numero in numbers:
        resultado = resultado * numero
    return resultado


def isiteven(num):
    return num % 2 == 0 and isitaninteger(num)


def isitaninteger(num):
    return num == int(num)


def main():
  print("Hello learners!")

if __name__=="__main__":
  main()