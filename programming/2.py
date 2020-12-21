# lab # 2
# задан массив из N натуральных чисел. найти среднее
# арифметическое и среднее геометрическое нечетных
# чисел.
import math


def sum_elements(data):
    if len(data) == 0:
        print("list is empty")
        return

    mean_sum = 0
    mean_squared = 0
    cnt = 0
    for i, element in enumerate(data):
        if i % 2 == 0:
            mean_sum += element
            mean_squared += math.sqrt(element ** 2)
            cnt += 1

    print(mean_sum / cnt)
    print(mean_squared / cnt)


if __name__ == '__main__':
    elements = [-5, 8, 7, -17, 22, 36, 16, 2]
    sum_elements(elements)
