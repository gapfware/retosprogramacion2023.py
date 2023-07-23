from datetime import datetime


def generate_random_number():
    return round(datetime.now().microsecond % 101)


def run():
    number = generate_random_number()
    print(number)


if __name__ == '__main__':
    run()
