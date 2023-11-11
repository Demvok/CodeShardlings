pets = [
    ('Fluffy', 'John', 'Connor', 28),
    ('Brown', 'Amelia', 'Sun', 22),
    ('Albedo', 'Gui', 'Zhong', 2800),
    ('Klee', 'Gui', 'Zhong', 2800)
]

result = {}
for pet in pets:
    result.setdefault((pet[1], pet[2], pet[3]), []).append(pet[0])

print(result)