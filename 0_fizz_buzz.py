# Escribir un programa que muestre en pantalla los números del 1 al 100, sustituyendo los múltiplos de 3 por la palabra “fizz”, los múltiplos de 5 por “buzz” y los múltiplos de ambos, es decir, los múltiplos de 3 y 5 (o de 15), por la palabra “fizzbuzz”.

def run():
    for i in range(1, 100 + 1):
        if i % 15 == 0:
            print(f"FizzBuzz {i}")
        elif i % 3 == 0:
            print(f"fizz {i}")
        elif i % 5 == 0:
            print(f"buzz {i}")


if __name__ == '__main__':
    run()
