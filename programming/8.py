# lab 8
#  задан целочисленный массив из 150 элементов.
# выделить в отдельный массив все его элементы, кратные 5.
import random


def f(elements):
    filtered = []

    for num in elements:
        if num % 5 == 0:
            filtered.append(num)

    return filtered


if __name__ == '__main__':
    elems = [random.randrange(150) for x in range(0, 150)]
    print(f'изначальный массив: {elems}')
    print(f'массив элементов, кратных 5: {f(elems)}')
