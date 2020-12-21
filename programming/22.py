# lab 22
# дан целочисленный массив А из N элементов.
# проверьте, есть ли в нем элементы, равные нулю. если есть,
# найдите номер первого из них, т. е. наименьшее i, при
# котором элемент ai = 0.


def f(elements):
    try:
        return elements.index(0)
    except ValueError:
        return -1


if __name__ == '__main__':
    list1 = [1, 56, 7, 0, 3, 2, 6, 2, 2, 1, 43]
    print(f'индекс первого элемента в списке: {list1}, равного нулю: {f(list1)}' if f(list1) != -1 else f'массив {list1} не содержит 0')
    list2 = [1, 56, 7, 2, 2, 1, 43]
    print(f'индекс первого элемента в списке: {list2}, равного нулю: {f(list2)}' if f(list2) != -1 else f'массив {list2} не содержит 0')