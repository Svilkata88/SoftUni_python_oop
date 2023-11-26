def read_next(*args):
    for elements in args:
        for element in elements:
            yield element


# test code:
gen = read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4})
for item in gen:
    print(item, end='')

print()
print('----------------------')

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i, end='')
