# Вспомогательная функция: формирование списка всех делителей числа
def all_dividers(n):
    temp_list = []
    if n==1:
        temp_list = [1]
    else:
        for i in range(1, n+1):
            if n % i == 0:
                temp_list.append(i)
    return temp_list

# Вспомогательная функция: проверка числа на простоту
def simplicity_checking(n):
    if len(all_dividers(n))>2:
        simplicity = 0
    else:
        simplicity = 1
    return simplicity

# Вывод списка всех делителей числа
def printing_all_dividers(n):
    print('Все делители числа', n, ':', all_dividers(n))

# Вывод самого большого простого делителя числа
def the_biggest_simple_divider(n):
    aux_list = all_dividers(n)
    number = 0
    for i in range(len(aux_list)):
        if simplicity_checking(aux_list[i]) == 1:
            number = aux_list[i]
    print('Наибольший простой делитель числа', n, 'равен', number)

# Вывод канонического разложения числа на простые множители
def canonical_decomposition(n):
    all_simple_numbers_list = []
    for i in range(2, n):
        if simplicity_checking(i) == 1:
            all_simple_numbers_list.append(i)

    temp_dict = {}
    for i in range(len(all_simple_numbers_list)):
        aux_number = n
        j = 0
        while aux_number % all_simple_numbers_list[i] == 0:
            aux_number = aux_number/all_simple_numbers_list[i]
            j+=1
        if j>0:
            temp_dict[all_simple_numbers_list[i]]= j
    print('Каноническое разложение для числа', n, '(число:степень):', temp_dict)

# Вывод самого большого делителя (не обязательно простого), не равного самому числу
def max_divider(n):
    aux_list = all_dividers(n)
    print('Самый большой делитель числа', n, '(не равный самому числу):', aux_list[len(aux_list)-2])