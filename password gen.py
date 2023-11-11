import random
print(*[[[elem.lower(), elem.upper()][random.randint(0,1)] for elem in chr(random.randint(65, 90))][0] for _ in range(int(input()))], sep='')