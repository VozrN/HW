def is_prime(func_summ):
    i = func_summ()
    is_pr = True
    for j in range(2, i):
        if i % j == 0:
            print('Составное')
            return func_summ
    print('Простое')
    return func_summ


@is_prime
def sum_three(*args):
    summ_args = sum(args)
    return (summ_args)


result = sum_three(2, 3, 6)
print(result)
