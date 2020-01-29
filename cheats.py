"""СПИСКИ"""
"""Вывести минимальное, максимальное, сумму"""
def test_min_max_sum():
    numbers = [1, 2, 3]
    print(min(numbers))
    print(max(numbers))
    print(sum(numbers, 10))


"""Вывести все элементы, которые меньше 5"""
def test_elem():
    # Перебор элементов
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for elem in a:
        if elem < 5:
            print(elem)   # [1, 1, 2, 3]

    # с помощью функции filter
    print(list(filter(lambda elem: elem < 5, a)))

    # списковое включение
    print([elem for elem in a if elem < 5])


'''Вывести строку в обратном порядке'''
# с помощью срезов
def test_is_palindrome():
    string = 'ABBA'
    print(string == string[::-1])    # True


# сравнить строку с её обратной версией
def test_is_palindrome2():
    string = 'ABBA'
    print(string == ''.join(reversed(string)))


'''возвести в квадрат все элементы списка.'''
def test_square():
    numbers = [1, 2, 3, 4, 5]
    print([number*number for number in numbers])  # [1, 4, 9, 16, 25]


'''Фильтрация списка'''
def test_list_filter():
    numbers = [1, 2, 3, 4, 5]
    print([number for number in numbers if number < 4])  # [1, 2, 3]


'''возвести в квадрат и фильтрация списка'''
def test_square_and_filter():
    numbers = [1, 2, 3, 4, 5]
    print([number*number for number in numbers if number < 4])  # [1, 4, 9]


'''Вывод списка'''
#  без кавычек
def test_print_list():
    recent_presidents = ['Борис Ельцин', 'Владимир Путин', 'Дмитрий Медведев']
    print('%s.' % ', '.join(recent_presidents))  #  Борис Ельцин, Владимир Путин, Дмитрий Медведев.


#  пронумеровать элементы
def test_print_list_enumerate():
    strings = ['a', 'b', 'c', 'd', 'e']
    for index, string in enumerate(strings):
        print(index, string)  # 0 a, 1 b и т.д


'''Проверка на вхождение подстроки'''
def test_item_in_str():
    string = 'Hi there'
    if 'Hi' in string:
        print('Success!')


'''Проверить что все значения в списке меньше 10'''
def test_num_less():
    numbers = [1, 2, 3, 4, 5, 65, 7, 8, 9]
    if all(number < 10 for number in numbers):
        print('Success!')


'''убедиться, что элементы списка уникальны.'''
#преобразовать его в сет и проверить, изменилась ли длина
def test_elem_is_unique():
    numbers = [1, 2, 3, 4]
    set(numbers)  # возвращает set([1,2,3,4])
    if len(numbers) == len(set(numbers)):
        print('List is unique!')


'''Вернуть список, который состоит из элементов, общих для этих двух списков'''
def test_equal_elem():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # через цикл
    result = []
    for elem in a:
        if elem in b:
            result.append(elem)
    print(result)  # [1, 1, 2, 3, 5, 8, 13]

    # через filter
    print(list(filter(lambda elem: elem in b, a)))  # [1, 1, 2, 3, 5, 8, 13]

    # списковым включением
    print([elem for elem in a if elem in b])  # [1, 1, 2, 3, 5, 8, 13]

    # привести оба списка к множествам и найти их пересечение:
    print(list(set(a) & set(b)))  # [1, 2, 3, 5, 8, 13]
    # Однако в таком случае каждый элемент встретится в результирующем списке лишь один раз,
    # т.к. множество поддерживает уникальность входящих в него элементов.
    # Первые два решения (с фильтрацией) оставят все дубли на своих местах.


'''СЛОВАРИ'''
# Создание словаря
def test_dict():
    print(dict(a=1, b=2, c=3))  # возвращает {'a': 1, 'b': 2, 'c': 3}


# распечатать словарь ключ - значение
def test_print_dict():
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    for key in dictionary:
        print(key, dictionary[key])


#  Преобразование списка в словарь
def test_list_as_dict():
    dict_as_list = [['a', 1], ['b', 2], ['c', 3]]
    dictionary = dict(dict_as_list)
    print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}


# получить и ключи, и значения в виде списка кортежей
def test_dict_as_list():
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    print(dictionary.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])


'''в Python объект считается false, только если он пуст. Это значит, что не нужно проверять длину строки, кортежа или словаря —
 достаточно проверить его как логическое выражение.'''
def test_example():
    my_object = '123'
    if my_object:
        print('my_object не пуст')


'''Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды'''
def test_convert_time():
    seconds = 1234565
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}d. {hours}h. {minutes}m. {seconds}s.')  # 14d. 6h. 56m. 5s.



