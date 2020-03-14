#developer Mikhailov. A

import time
from random import randint
start = time.time()

def main():
    try:
        if binsearch(a, x):
            return ind(a, x)

    except IndexError:
        return None


def binsearch(a, x):
    middle = len(a) // 2
    if a[middle] < x:
        return binsearch(a[middle + 1:], x)
    elif a[middle] > x:
        return binsearch(a[:middle], x)
    return True


def ind(a, x):
    index = 0
    if a[0] == x:
        return index
    return ind(a[1:], x) + (index + 1)
x = int(input('Введите целое число:'))
a = []
for k in range(1000):
    a.append(randint(1, 1000))
a.sort()
print(a)
print(main())
print(f"{(time.time() - start)} миллисекунд")
