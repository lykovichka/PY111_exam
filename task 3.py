"""Сорт
Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
Задача: отсортировать массив наиболее эффективным способом """
import random
import time


def sort_1(array: list) -> list:
    """ Bubble sort function"""

    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]

    return array


def sort_2(array: list) -> list:
    """ Quick sort function """
    if len(array) <= 1:
        return array
    num_random = random.choice(array)
    left_side = [num for num in array if num < num_random]
    equals = [num_random] * array.count(num_random)

    right_side = [num for num in array if num > num_random]
    return sort_2(left_side) + equals + sort_2(right_side)


arr = [random.randint(13, 27) for _ in range(10**4 + 1)]

if __name__ == '__main__':
    time_list_1 = []
    time_list_2 = []
    for i in range(11):
        start = time.perf_counter()
        sort_2(arr)
        time_list_2.append(time.perf_counter() - start)
        sort_1(arr)
        time_list_1.append(time.perf_counter() - start)

    print(f"Bubble sort time: {sum(time_list_1) / 10}, Quick sort time: {sum(time_list_2) / 10}")
    # Bubble sort time: 8.460435769998004, Quick sort time: 0.0033987200004048645
    # при arr = [random.randint(13, 27) for _ in range(10**4 + 1)]
