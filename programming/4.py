# lab 4
# определить количество перемен знака у элементов задан
# ного массива из М элементов.


def check_diff_sign(num1, num2):
    # у нуля нет знака, потому он не участвует в сравнении
    if num1 > 0 and num2 < 0:
        return True
    if num1 < 0 and num2 > 0:
        return True

    return False


def f(elements):
    if len(elements) < 2:
        return 0

    counter = 0
    for i in range(0, len(elements) - 1):
        if check_diff_sign(elements[i], elements[i + 1]):
            counter += 1

    return counter


if __name__ == '__main__':
    # 8 раз менялся знак
    print(f([15, 6, 7, -4, 3, -2, 2, 2, -15, 6, -7, -8, -9, -10, 2]))
