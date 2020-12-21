# lab 5
# заменить на единицу минимальный по абсолютной величине элемент заданного массива Х = (х1, х2, ..., хn). если
# минимальных компонентов несколько, заменить их все.


def f(elements):
    if len(elements) == 0:
        return []

    minimal = elements[0]
    abs_minimal = abs(minimal)

    for i in range(len(elements)):
        if abs(elements[i]) < abs_minimal:
            minimal = elements[i]
            abs_minimal = abs(elements[i])

    for i in range(len(elements)):
        if elements[i] == minimal:
            elements[i] = 1

    return elements


if __name__ == '__main__':
    print(f([-5, 20, 15, 6, 3, 22, 3]))
    print(f([-5, -2, 15, -2, 3, 22, 3]))
