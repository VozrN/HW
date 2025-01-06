def calculate_structure_sum(*args):
    sum_whole = 0
    for i in args:
        if isinstance(i, int):
            sum_whole += i
        elif isinstance(i, str):
            sum_whole += len(i)
        elif isinstance(i, list):
            sum_whole += calculate_structure_sum(*i)
        elif isinstance(i, bool):
            sum_whole += i
        elif isinstance(i, float):
            sum_whole += i
        elif isinstance(i, tuple):
            sum_whole += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            sum_whole += calculate_structure_sum(*i.items())
        elif isinstance(i, set):
            sum_whole += calculate_structure_sum(*i)
    return sum_whole


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
