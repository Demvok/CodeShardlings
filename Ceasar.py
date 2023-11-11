def code(message, key):
    alph_lower = [elem for elem in 'abcdefghijklmnopqrstuvwxyz']
    alph_capital = [elem.upper() for elem in alph_lower]
    s = ''
    for elem in message:
        if elem in alph_lower:
            s += alph_lower[(alph_lower.index(elem)+key)%26]
        elif elem in alph_capital:
            s += alph_capital[(alph_capital.index(elem)+key)%26]
        else:
            s += elem
    return s

def code_rus(message, key):
    alph_lower = [elem for elem in 'абвгдежзийклмнопрстуфхцчшщъыьэюя']
    alph_capital = [elem.upper() for elem in alph_lower]
    s = ''
    for elem in message:
        if elem in alph_lower:
            s += alph_lower[(alph_lower.index(elem)+key)%32]
        elif elem in alph_capital:
            s += alph_capital[(alph_capital.index(elem)+key)%32]
        else:
            s += elem
    return s

def quantity(inp):
    letters = {letter: inp.lower().count(letter) for letter in set([elem.lower() for elem in inp if elem.isalpha()]) }
    return {key: value for key, value in sorted(letters.items(), key=lambda x: x[1], reverse=True) }

def print_quantity(d):
    print(*[ f'{key}:{value}' for key, value in d.items() ], sep=' ')

inp = """8 Teams in each gender competed at the Championship, including two from Western Canada, two from Ontario, two from Quebec, and two from Atlantic Canada, including the hosts Memorial University.
The Memorial Sea-Hawks became the men's champions, while the Laurier Golden Hawks became the women's champions."""

def read_from_file(name):
    with open(name, 'r', encoding='UTF-8') as file:
        return  file.read().replace('\n', ' ')

def write_csv(d):
    with open('analysis.csv', 'w', encoding='UTF-8') as file:
        for key, value in d.items():
            file.write(f'{key},{value}\n')

# inp = read_from_file('goats.txt')

# print(inp)
quant = quantity(inp)
print_quantity(quant)
write_csv(quant)
inp = code(inp, -7)
print_quantity(quant)