def myyield():
    print('即将')
    yield 2
    yield 3
    yield 5
    yield 7
    print('3')

gen = myyield()
print(gen)

it = iter(gen)

print(next(it))

print(next(it))