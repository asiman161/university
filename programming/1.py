# lab 1
# дан целочисленный массив А из N элементов. проверьте,
# есть ли в нем элементы, равные нулю. если есть, найдите
# номер первого из них, т. е. наименьшее i, при котором
# элемент ai = 0.

if __name__ == '__main__':
    lists = [
        [1, 2, 3, 4],
        [4, 5, 1, 0, 22],
        [0, 1, 2],
        [42, 1, 2],
        [5, 2, 0],
    ]

    for arr in lists:
        try:
            print(f'index of zero element is: {arr.index(0)}')
        except ValueError:
            print(f'{arr} does not have zero')
