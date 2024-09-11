def print_params(a=1, b='строка', c=True):
    print(a,b,c)

print_params()
print_params(1,25,[1,2,3])

values_list=('печать', 23.1, [4,6])
values_dict={'a':5, 'b':'fun', 'c':False}
print_params(*values_list)
print_params(**values_dict)

values_list_2=([1,2], 'sun')
print_params(*values_list_2, 42)

