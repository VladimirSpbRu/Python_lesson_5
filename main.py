from divisor_master import simplicity_checking
from divisor_master import printing_all_dividers
from divisor_master import the_biggest_simple_divider
from divisor_master import canonical_decomposition
from divisor_master import max_divider

natural_number = int(input('Введите натуральное число: '))

if simplicity_checking(natural_number) == 1:
    print('Число', natural_number, 'является простым.')
else:
    print('Число', natural_number, 'не является простым.')

printing_all_dividers(natural_number)

the_biggest_simple_divider(natural_number)

canonical_decomposition(natural_number)

max_divider(natural_number)