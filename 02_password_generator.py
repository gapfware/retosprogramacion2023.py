"""
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 * """
from random import choice


class LenghtException(Exception):
    def __init__(self, message='No se puede generar contraseña, longitud no valida.') -> None:
        self.message = message
        super().__init__(self.message)


def generate_password(length=8, has_uppers=False, has_numbers=False, has_symbols=False):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    NUMBERS = '1234567890'
    CAPS = characters.upper()
    SYMBOLS = '~`@#$%^&*()_+{}[]\|;:/?<>,.-'
    password = ''

    try:
        if length < 8 or length > 16:
            raise LenghtException()
        if has_uppers:
            characters += CAPS
        if has_numbers:
            characters += NUMBERS
        if has_symbols:
            characters += SYMBOLS

        for char in range(length):
            password += choice(characters)

    except LenghtException as err:
        print(f"Error: {err}")

    return password


def run():
    generated_password = generate_password(length=28, has_numbers=True)
    print(generated_password)


if __name__ == '__main__':
    run()