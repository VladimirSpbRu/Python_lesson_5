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

# Автотесты для функции, формирующей список всех делителей
def test_all_dividers_1():
    if all_dividers(6) == [1, 2, 3, 6]:
        print('Test 1 is passed.')
    else:
        print('Test 1 is failed.')

def test_all_dividers_2():
    assert all_dividers(6) == [1, 2, 3, 6]

# Вспомогательная функция: проверка числа на простоту
def simplicity_checking(n):
    if len(all_dividers(n))>2:
        simplicity = 0
    else:
        simplicity = 1
    return simplicity

# Автотесты для функции, проверяющей число на простоту
def test_simplicity_checking_1():
    if simplicity_checking(6) == 0:
        print('Test 2 is passed.')
    else:
        print('Test 2 is failed.')

def test_simplicity_checking_2():
    if simplicity_checking(7) == 1:
        print('Test 3 is passed.')
    else:
        print('Test 3 is failed.')

def test_simplicity_checking_3():
    assert simplicity_checking(7) == 1
