# lab 19
# составить программу, дающую ответ «да» или «нет» в
# зависимости от того, встречается ли число 7 в заданном
# целочисленном массиве А, состоящем из N элементов.

def f(elements):
    try:
        elements.index(7)
        return "ДА"
    except ValueError:
        return "НЕТ"


if __name__ == '__main__':
    print(f([1, 5, 7, 2, 6, 2, 5, 12, 6, 3]))
    print(f([1, 5, 1, 6, 3, 1, 2]))
