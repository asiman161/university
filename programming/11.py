# lab 11
# задан массив А из n элементов и вещественное число
# с. переписать в новый массив В все элементы из А, которые
# больше с.


def f(elements, n):
    return [x for x in elements if x > n]


if __name__ == '__main__':
    print(f([-2, -1, 0, 1, 2, 3, 4, 5, 5.24, 5.26, 6, 7, 8, 9, 10], 5.25))
