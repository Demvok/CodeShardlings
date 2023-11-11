from faker import Faker

fake = Faker()
res = []
for _ in range(25):
    res.append(f"\"{fake.name()}\"")
print(', '.join(res))
