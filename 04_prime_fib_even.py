from math import sqrt


def is_even(number: int):
    return number % 2 == 0


def is_square(n: int):
    s = int(sqrt(n))
    return s*s == n


def is_fib(number: int):
    fib = False
    if is_square(5*number*number + 4) or is_square(5*number*number - 4) :
        fib = True
    return fib


def is_prime(number: int):
    prime_number = True
    for i in range(2, number):
        if number % i == 0:
            prime_number = False
            break
    return prime_number

def check_prime_fib_even(number: int):
    prime = "Es primo" if is_prime(number) else "No es primo"
    fib = "es fibonacci" if is_fib(number) else "no es fibonacci"
    even = "es par" if is_even(number) else "es impar"
    return f"El Numero {number} {prime}, {fib} y {even}"



def run():
    print(check_prime_fib_even(2))
    print(check_prime_fib_even(7))
    print(check_prime_fib_even(25))


if __name__ == '__main__':
    run()
