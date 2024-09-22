def calculate_structure_sum(data_structure):
    summator = 0
    if isinstance(data_structure, dict):
        for key, values in data_structure.items():
            summator += calculate_structure_sum(key)
            summator += calculate_structure_sum(values)
    elif isinstance(data_structure, (list, tuple, set)):
        for component in data_structure:
            summator += calculate_structure_sum(component)
    elif isinstance(data_structure, (int, float)):
        summator += data_structure
    elif isinstance(data_structure, str):
        summator += len(data_structure)
    return summator


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
