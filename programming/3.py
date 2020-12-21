# lab 3
# ввести массив A = ( a1, a2, ..., an). просматривая его элементы слева направо, заменить в нем каждый нулевой
# элемент полусуммой последующего и предыдущего. если
# a1 = 0, заменить его на a2, если an = 0, заменить его на
# an−1.


def f(elements):
    if len(elements) < 2:
        return elements
    if elements[0] == 0:
        elements[0] = elements[1]
    if elements[-1] == 0:
        elements[-1] = elements[-2]

    for i in range(1, len(elements) - 1):
        if elements[i] == 0:
            v = (elements[i - 1] + elements[i + 1]) / 2
            elements[i] = v
    return elements


if __name__ == '__main__':
    print(f([0, 5, 2, 6, 0, 7, 8, 0, 44, 0]))
    # 5,5,2,6,6.5,7,8,26,44,44
