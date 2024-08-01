def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 'Тетрис', b = {'apple': 15}, c = False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['Cat', 159, [47, 58]]
values_dict = {'a': 'rain', 'b': 25, 'c': 2.5}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3.14, 'Число Пи' ]
print_params(*values_list_2, 42)
