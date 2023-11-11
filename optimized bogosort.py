from random import *
# arr = list(range(1, 11))
# shuffle(arr)
arr = [randrange(51) for _ in range(20)]

def sortCheck(array):
    flag = True
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            flag = False
            break
    return flag

srtd = []
cell = len(arr)
cost = 0
costed = []
while len(arr) != 0:
    print(str(srtd) + ' ' + str(arr))
    if arr[0] == min(arr):
        costed.append(cost+1)
        cost = 0
        srtd.append(arr.pop(0))
    else:
        shuffle(arr)
        cost += 1
print(srtd)
print(f'Steps - {costed}') 