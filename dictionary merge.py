def merge(values):
    d = {}
    for dic in values:
        for key, value in dic.items():
            d.setdefault(key, set()).add(value)
    return d

print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))