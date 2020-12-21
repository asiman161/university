# lab 17
# даны целые а, х1, х2, ..., xn. определить, каким по счету
# идет в последовательности х1, х2, ..., xn член, равный а.
# если такого члена нет, то ответом должно быть число 0.


def f(elements, n):
    try:
        return elements.index(n)
    except ValueError:
        return 0


if __name__ == '__main__':
    print(f([2, 4, 5, 6, 7, 1, 15], 7))
