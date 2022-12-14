"""Задача консенсуса DNA ридов
При чтении DNA последовательностей могут возникать единичные ошибки,
выражающиеся в неверной букве в строке.
Для решения данной проблемы требуемое место читается несколько раз,
после чего строится консенсус-строка, в которой на каждом месте будет стоять тот символ,
что чаще всего встречался в этом месте суммарно во всех чтениях.
Т.е. для строк ATTA ACTA AGCA ACAA
консенсус-строка будет ACTA (в первой ячейке чаще всего встречалась A, во второй – C,
в третьей – Т, в четвертой – снова А).
Для входного списка из N строк одинаковой длины построить консенсус-строку."""

array = [['A', 'T', 'T', 'A'],
         ['A', 'C', 'T', 'A'],
         ['A', 'G', 'C', 'A'],
         ['A', 'C', 'A', 'A']]


def transport(matr):
    """ Функция Транспонирование матрицы (меняем столбцы со строками местами)"""
    length = len(matr)
    for i in range(length - 1):
        for j in range(i + 1, length):
            matr[i][j], matr[j][i] = matr[j][i], matr[i][j]
    return matr


def counter(matr):
    """ Функция подсчета наиболее часто встречающихся символов"""
    matr = transport(matr)
    result = []

    for i in range(len(matr)):
        set_ = set(matr[i])
        most_value = None  # наиболее часто встречаемое значение
        sum_most_value = 0  # его количество
        for symb in set_:
            q = matr[i].count(symb)
            if q > sum_most_value:
                sum_most_value = q
                most_value = symb
        result.append(most_value)
    return result


print(counter(array))
