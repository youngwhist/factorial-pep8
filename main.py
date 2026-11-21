"""Вычисление факториала целого неотрицательного числа."""
import sys


def factorial(n):
    """Возвращает n! или None для отрицательного n."""
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


def main(argv):
    if len(argv) != 2:
        print('Использование: python3 main.py <целое число>')
        return 1
    try:
        n = int(argv[1])
    except ValueError:
        print(f'Ошибка: «{argv[1]}» — не целое число')
        return 1
    value = factorial(n)
    if value is None:
        print('Ошибка: факториал определён только для n >= 0')
        return 1
    print(f'{n}! = {value}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
